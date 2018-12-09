# coding=utf-8
import pymysql


class MySQLUtil(object):

    def __init__(self, ip: str, port: int, database: str, user: str, password: str):
        self.ip = ip
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.db_online = pymysql.connect(self.ip, self.user, self.password, self.database, self.port)
        self.cursor = self.db_online.cursor()

    # db_online = pymysql.connect("10.188.36.15", "all_open_r", "DBVs9XckpCGkerNF", "tc_settlement", 5408)

    def executeQuery(self, sql, callback):
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            for row in results:
                callback(row)
        except:
            print("Error")

    def closeDB(self):
        self.db_online.close()
