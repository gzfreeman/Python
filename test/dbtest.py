# -*- coding: gbk -*-

import dbpool
import os




if __name__ == '__main__':
    dbpool_util = dbpool.DbPoolUtil()
    #dbpool_util.execute_iud("insert into TD_S_OPCODE values('2014vvv3333','这是一个坑','abcd12345','45654758609')")
    dbpool_util.execute_query_single("select * from TD_S_OPCODE")
