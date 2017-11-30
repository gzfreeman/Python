import  os
import configparser
import smtplib

from email.mime.text import MIMEText
from email.header import Header
config=configparser.ConfigParser()
config.read("config.ini")
monurl = config.get("mon_url", "qdy_url")
mailhost = config.get("mailinfo","m_host")
mailuser = config.get("mailinfo","m_user")
mailpass = config.get("mailinfo","m_pass")
mail_receiver = config.get("mailinfo","m_receiver")
mail_sender = "freeman"
message = MIMEText(monurl, 'plain', 'utf-8')
subject = 'sys_info'
try:
    print(mailhost)
    smtpObj=smtplib.SMTP(mailhost,25)
    #smtpObj.set_debuglevel(1)
    smtpObj.login(mailuser,mailpass)
    smtpObj.sendmail(mail_sender, mail_receiver, message.as_string())
    print ("邮件发送成功")
except smtplib.SMTPException:
    print ("Error: 无法发送邮件")