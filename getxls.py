import pymysql as pms
import openpyxl
import  datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import smtplib
import traceback



#获取昨天的日期
yesterday = (datetime.today() + timedelta(days = -1)).strftime("%Y-%m-%d")

def getdatas(sql):
    ##一个传入sql导出数据的函数
    con = pms.connect(host="",user="",paswd="",database="",port="",charset="")
    cur = con.cursor()
    cur.execute(sql)
    datas = cur.fetchall()
    cur.close()
    return  datas


def getfield(sql):
    ##一个传入sql导出字段
    con = pms.connect(host="",user="",paswd="",database="",port="",charset="")
    cur = con.cursor()
    cur.execute(sql)
    fields = cur.description
    cur.close()
    return  fields

def getexcel(data,field,file):
    new = openpyxl.Workbook()
    sheet = new.active
    sheet.title = "数据展示"
    for col in range(len(field)):
        _ = sheet.cell(row=1,column=col+1,value=u'')
    for row in range(len(data)):


##创建邮件
def create_mail(email_from,email_to,email_subject,email_text,annex_path,annex_name):
    message = MIMEMultipart()
    message.attach(MIMEText(email_text,'plain','utf-8'))
    message['From'] = Header(email_from,'utf8')
    message['To'] = Header(email_to, 'utf8')
    message['Subject'] = Header(email_subject, 'utf8')
    #读取附件的内容
    attl = MIMEText(open(annex_path,"rb").read(),'base64','utf-8')
    attl["Content-Type"] = 'application/octet-strem'
    attl["Content-Disposition"] = 'attachment; filename=' + annex_name
    message.attach(attl)
    return  message


#发送邮件
def send_mail(sender,password,receiver,msg):
    try:
        server = smtplib.SMTP_SSL("aaa.aaa.com",465)
        server.helo()
        server.login(sender,password)
        server.sendmail(sender,receiver,msg.as_string())
        print("邮件发送成功")
        server.quit()
    except Exception:
        print(traceback.print_exc())
        print("邮件发送失败")


