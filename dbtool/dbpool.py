# -*- coding: utf-8 -*-

from PropertiesUtil import prop
from DBUtils.PooledDB import PooledDB
import importlib
import cx_Oracle


class DbPoolUtil(object):
    def __init__(self, config_file='db.properties'):
        properties_dic = prop.get_config_dict(config_file)
        self.__db_type = properties_dic['dbtype']
        if self.__db_type == "mysql":
            config = {
                #'host': properties_dic['dbip'],
                #'port': int(properties_dic['dbport']),
                #'db': properties_dic['database'],
                #'user': properties_dic['username'],
                #'password': properties_dic['password'],
                #'charset': "utf8"
            }
            db_creator = importlib.import_module("cx_Oracle")
            self.__pool = PooledDB(db_creator, maxcached=50, maxconnections=200, maxusage=200, **config)
        elif self.__db_type == "oracle":
            config = {
                'user': properties_dic['username'],
                'password': properties_dic['password'],
                'dsn': "/".join(
                    [":".join([properties_dic['dbip'], properties_dic['dbport']]), properties_dic['servicename']])
            }
            db_creator = importlib.import_module("cx_Oracle")
            self.__pool = PooledDB(db_creator, maxcached=50, maxconnections=200,maxusage=200,**config)

        else:
            raise Exception("unsupported database type " + self.__db_type)
    ##查询##
    def execute_query(self, sql, args=()):
        result = ()
        conn = self.__pool.connection()
        cur = conn.cursor()
        try:
            cur.execute(sql, args)
            result = cur.fetchall()
        except Exception as e:
            print('异常信息:' + str(e))
        cur.close()
        conn.close()
        return result

    ##查询单条记录
    def execute_query_single(self, sql, args=()):
        result = ()
        conn = self.__pool.connection()
        cur = conn.cursor()
        try:
            cur.execute(sql, args)
            result = cur.fetchone()
        except Exception as e:
            print('异常信息:' + str(e))
        cur.close()
        conn.close()
        return result

    def execute_iud(self, sql, args=()):
        conn = self.__pool.connection()
        cur = conn.cursor()
        count = 0
        try:
            result = cur.execute(sql, args)
            conn.commit()
            if self.__db_type == "mysql":
                count = result
        except Exception as e:
            print('异常信息:' + str(e))
            conn.rollback()
        cur.close()
        conn.close()
        return count
    #
    # def execute_many_iud(self, sql, args):
    #     conn = self.__pool.connection()
    #     cur = conn.cursor()
    #     count = 0
    #     try:
    #         result = cur.executemany(sql, args)
    #         conn.commit()
    #         if self.__db_type == "mysql":
    #             count = result
    #         if self.__db_type == "sqlite3":
    #             count = result.rowcount
    #     except Exception as e:
    #         print('异常信息:' + str(e))
    #         conn.rollback()
    #     cur.close()
    #     conn.close()
    #     return count



