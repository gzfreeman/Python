import os
import subprocess
env_dist = os.environ
#for key in env_dist:
    #print (key + ' : ' + env_dist[key])

ENV_PATH="/u01/oracle/.bash_profile"

##定义数据库账户和密码
username="petl"
password="petl"
def base(cmd):
    if subprocess.call(cmd, shell=True):
        raise Exception("{} 执行失败".format(cmd))

##异常处理，shell执行后获取返回的状态值，如果执行失败，需要返回shell错误的信息

def read_env():
    if(os.path.exists(ENV_PATH)):
        #加载环境变量
        base("source ENV_PATH")
    else:
        print("can not find the file")

def test_error():
    base("hos")


def create_dir():
    if (not os.path.exists("/var/cmdb/db")):
        base("sudo mkdir -p /var/cmdb/db")



test_error()