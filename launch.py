# -*- coding: utf-8 -*-
import configparser
import os

__author__ = 'luoqian'

from fetcher.BlessFetcher import *
from fetcher.GuestFetcher import *
from mailServer.mailServer import *

if __name__ == '__main__':
    print('婚礼请柬统计开始')
    # datasource info
    ip = "localhost"
    port = 3306
    database = "wedding"
    user = "xxxx"
    password = "xxxx"
    mysqlUtil = MySQLUtil(ip, port, database, user, password)
    # fetch data
    blessFetcher = BlessFetcher(mysqlUtil)
    guestFetcher = GuestFetcher(mysqlUtil)

    # assemble mailServer
    guestContent = ""
    blessContent = ""
    totalNum = 0

    # mail info
    from_addr = "xxxx@163.com"
    from_name = "婚礼请柬统计"
    from_password = "xxxx"
    from_stmp_server = MailServer.NETEASY_163

    TYPE_SPLIT = "===================================================================="
    ITEM_SPLIT = "-----------------------------------------------------------------------------------------------------"

    mailSender = MailSender(from_addr, from_name, from_password, from_stmp_server)


    def handleBlessData(data):
        global blessContent
        name = data[1]
        time = data[3]
        msg = data[2]
        bless = name + '（' + time + '）：' + '\r\n' + msg + '\r\n'
        blessContent = blessContent + bless + ITEM_SPLIT + '\r\n'


    blessFetcher.fetch(lambda data: handleBlessData(data))


    def handleGuestData(data):
        global guestContent
        global totalNum
        totalNum = totalNum + int(data[3])
        guestName = '姓名:%s' % data[1]
        guestPhone = '电话:%s' % (data[2] if data[2] != 0 else '无')
        guestNum = '人数:%s' % (data[3] if data[3] != 0 else '有事不来')
        # guestIp = 'ip:%s' % data[4]
        guest = guestName + '\r\n' + guestPhone + '\r\n' + guestNum + '\r\n'
        guestContent = guestContent + guest + ITEM_SPLIT + '\r\n'


    guestFetcher.fetch(lambda data: handleGuestData(data))

    mailContent = "来宾统计：\r\n" + TYPE_SPLIT + "\r\n"
    mailContent = mailContent + "预计参与人数：" + str(totalNum) + "\r\n"
    mailContent = mailContent + ITEM_SPLIT + "\r\n"
    mailContent = mailContent + guestContent
    mailContent = mailContent + "\n\n"
    mailContent = mailContent + "祝福收集：\r\n" + TYPE_SPLIT + "\r\n"
    mailContent = mailContent + blessContent

    # read config
    config = configparser.ConfigParser()
    config.read('config.ini', "utf-8")
    mailList = config.items("MAIL_LIST")
    mailSubject = "婚礼请柬统计"
    for email in mailList:
        toAddr = email[0]
        toName = email[1]
        mailSender.sendTextMail(toAddr, toName, mailSubject, mailContent)

    mailSender.quitMail()
    print('婚礼请柬统计结束')
    os.system("pause")
