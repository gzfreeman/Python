import requests
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

#登录时需要POST的数据
data = {'account':'meiysh',
        'password':'Dic99e',
        'goto:http':'//112.94.22.222:5050/newzentao/www/index.php?m=my&f=index',
       }

#设置请求头
headers = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}

#登录时表单提交到的地址
login_url = 'http://112.94.22.222:5050/newzentao/www/index.php?m=user&f=login'

#构造Session
session = requests.Session()

resp = session.post(login_url, data)

#登录后才能访问的网页
url = 'http://112.94.22.222:5050/newzentao/www/index.php?m=my&f=index'

#发送访问请求
resp = session.get(url)

print(resp.content.decode('utf-8'))