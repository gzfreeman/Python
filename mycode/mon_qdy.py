import  os
import configparser
import smtplib
from email.mime.text import MIMEText
from email.header import Header

config=configparser.ConfigParser()
config.read("config.ini")
mon_url = config.get("mon_url", "qdy_url")
mail_host = config.get("mailinfo","m_host")
mail_user = config.get("mailinfo","m_user")
mail_pass = config.get("mailinfo","m_pass")
mail_receiver = config.get("mailinfo","m_receiver")
mail_sender = "kalos1121@163.com"
message = MIMEText(mon_url, 'plain', 'utf-8')
#message['From'] = Header("菜鸟教程", 'utf-8')
#message['To'] = Header("测试", 'utf-8')
subject = 'sys_info'

try:
    #smtpObj = smtplib.SMTP(mail_host)
    print ("this is "+ mail_host)
    smtpObj=smtplib.SMTP(mail_host,25)
    smtpObj.set_debuglevel(1)
    smtpObj.login(mail_sender,mail_pass)
    smtpObj.sendmail(mail_sender, mail_receiver, message.as_string())
    print ("邮件发送成功")
except smtplib.SMTPException:
    print ("Error: 无法发送邮件")