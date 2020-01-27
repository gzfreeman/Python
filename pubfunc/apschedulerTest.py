from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
import datetime
import os
import subprocess
import logging
env_dist = os.environ

ENV_PATH="/u01/oracle/.bash_profile"
##定义文件路径
dataFilePath="/u01/oracle/python_code/"
currentDate=datetime.datetime.now().strftime('%Y%m%d')
fileSuffix=".txt"
#fullPath=dataFilePath+"zq_"+currentDate+fileSuffix
fullPath="/u01/oracle/JZPT_CHNL_MDSY_201905.txt"


logging.basicConfig(level=logging.INFO,
                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                     datefmt='%Y-%m-%d %H:%M:%S',
                     filename='log1.txt',
                     filemode='a')


##定义每天生成新的jobid
def newJobid():
    pass

##定义执行shell命令
def base(cmd):
    if subprocess.run(cmd, shell=True,check=True):
        raise Exception("{} 执行失败".format(cmd))

##读取用户环境变量
def read_env():
    if(os.path.exists(ENV_PATH)):
        base("source ENV_PATH")
        #base("echo $ORACLE_HOME")
    else:
        print("can not find the file")

##加入异常处理，例如入库失败的返回信息，命令执行错误信息
def do_exception():
    pass


def stop_task():
    print(scheduler.get_jobs())
    scheduler.pause_job('job_id')
    scheduler.remove_job('job_id')
    return "success"

##检查文件存在后执行入库操作
def impData():
    if(os.path.exists(fullPath)):
        base('sqlldr rptuser/ic90oiPh control=/u01/oracle/JZPT_CHNL_MDSY_MODEL.ctl')
    else:
        print("no envfile")

##测试用
def writeFile():
    pass


##检查作业状态
def checkJobStatus():
    pass


scheduler = BlockingScheduler()
scheduler.add_job(func=impData, trigger='cron', second='*/5')
scheduler._logger = logging
scheduler.start()


