# -*- coding: utf-8 -*-
__author__ = 'luoqian'

from datasource.MySQLUtil import *


class BlessFetcher(object):

    def __init__(self, mysqlUtil: MySQLUtil):
        self.mysqlUtil = mysqlUtil

    def fetch(self, callback):
        sql = "SELECT * FROM bless order by id desc"

        self.mysqlUtil.executeQuery(sql, lambda data: callback(data))
