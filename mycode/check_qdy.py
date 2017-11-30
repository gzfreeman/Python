
# -*- coding: UTF-8 -*-
#author  Marco
import socket
import smtplib
import urllib.request

test_host = 'http://www.wom186.com/qdy'
mail_options = {
    'server':'smtp.163.com',
    'port':25,
    'user':'kalos1121@163.com',
    'pwd':'mys007',
    'send_to':'meiysh@op-mobile.com.cn',
}


def url_request(host,port=80):
    try:
        response = urllib.request.urlopen(host)
        response_code = response.getcode()
        if 200 == response_code:
            return response_code
        else:
            return True
    except IOError as e:
        return False

def send_email(mail,host,status):
    smtp = smtplib.SMTP()
    smtp.connect(mail['server'], mail['port'])
    smtp.login(mail['user'],mail['pwd'])
    msg="From:%s\rTo:%s\rSubject:服务器: %s 挂了 !状态码:%s\r\n" \
         % (mail['user'],mail['send_to'],host,status)
    smtp.sendmail(mail['user'],mail['send_to'], msg)
    smtp.quit()

def check_status(host,port=80):
    s = socket.socket()
    ret_msg = []
    try:
        s.connect((host,port))
        return True
    except socket.error as e:
        return False

if __name__=='__main__':
    status = url_request(test_host)
    if status is not True and status is not None:
        send_email(mail_options,test_host,status)
        
    else:
        pass