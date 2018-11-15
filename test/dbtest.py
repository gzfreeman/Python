# -*- coding: gbk -*-

import dbtool.dbpool
import json

if __name__ == '__main__':
    dbpool_util = dbtool.dbpool.DbPoolUtil()
    # dbpool_util.execute_iud("insert into TD_S_OPCODE values('2014vvv3333','这是一个坑','abcd12345','45654758609')")
    print(json.dumps(dbpool_util.execute_query("select * from jc_site")))
