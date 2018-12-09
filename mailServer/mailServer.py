# -*- coding: utf-8 -*-
__author__ = 'luoqian'

from email.utils import formataddr

from email.mime.text import MIMEText

import smtplib


class MailServer(object):
    NETEASY_163 = ['smtp.163.com', 25]
    QQ = ['smtp.qq.com', 25]
    GOOGLE = ['smtp.google.com', 25]


class MailSender(object):
    from_addr = ''
    password = ''
    smtp_server = ''
    from_name = ''
    server = None

    def __init__(self, from_addr, from_name, from_password, from_stmp_server: MailServer):
        self.from_addr = from_addr
        self.from_name = from_name
        self.password = from_password
        self.smtp_server = from_stmp_server
        try:
            self.server = smtplib.SMTP(from_stmp_server[0], from_stmp_server[1])
            self.server.set_debuglevel(1)
            self.server.login(from_addr, from_password)
        except smtplib.SMTPException:
            print('Login Error')

    def sendTextMail(self, to_addr, to_name, subject, content):
        msg = MIMEText(content, 'plain', 'utf-8')
        msg['From'] = formataddr([self.from_name, self.from_addr])
        msg['To'] = formataddr([to_name, to_addr])
        msg['Subject'] = subject
        try:
            self.server.sendmail(self.from_addr, [to_addr], msg.as_string())
        except smtplib.SMTPException:
            print('Send Error')

        print("发送成功 - [" + to_name + ":" + to_addr + "] - [" + subject + "]:\r\n" + content)

    def quitMail(self):
        self.server.quit()
