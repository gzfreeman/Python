import  paramiko
import re
hostname = '10.191.12.43'
port = 22
username = 'fjkuser'
password = 'NProdfjk'
##定义本地目录
localPath=""
##定义执行时间格式
t=paramiko.Transport((hostname,port))
t.connect(username=username,password=password)

sftp = paramiko.SFTPClient.from_transport(t)


filelist=sftp.listdir(path="/download")

pattern = '20191126' + '.txt'

for i, element in enumerate(filelist):
    ##未能完成匹配对应规则
    if element.re.search('20191127*_OrderCenter_YZS_GD.txt') != -1:
        pass
        #sftp.get(filelist[i],"d:/mycode/python/yzs/"+filelist[i])
        #filelist[i].pre
        #print("yes")



#sftp.close()
#ssh = paramiko.SSHClient()  #创建ssh对象
#ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  #允许连接不在know_hosts文件中的主机
#ssh.connect(hostname=hostname,port=port,username=username,password=password) #连接服务器
#stdin, stdout, stderr = ssh.exec_command("ls -ltr")#执行命令
#print(stdout.read().decode('utf-8'))

#20191121201625_OrderCenter_YZS_GD.txt 查找匹配符合格式

