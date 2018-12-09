# -*- coding: utf-8 -*-
__author__ = 'luoqian'

from datasource.MySQLUtil import *


class GuestFetcher(object):

    def __init__(self, mysqlUtil: MySQLUtil):
        self.mysqlUtil = mysqlUtil

    def fetch(self, callback):
        sql = "SELECT * FROM guest"

        self.mysqlUtil.executeQuery(sql, lambda data: callback(data))
