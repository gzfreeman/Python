
#coding=utf-8
import json

import urllib3
# based url and required header
url = "http://monitor.example.com/api_jsonrpc.php"
header = {"Content-Type": "application/json"}
# auth user and password
data = json.dumps(
{
    "jsonrpc": "2.0",
    "method": "user.login",
    "params": {
    "user": "Admin",
    "password": "jnadmin123"
},
"id": 0
})
# create request object
request = urllib3(url,data)
for key in header:
    request.add_header(key,header[key])
# auth and get authid
try:
    result = urllib3.urlopen(request)
except urllib3.exceptions as e:
    print ("Auth Failed, Please Check Your Name And Password:"),e.code
else:
    response = json.loads(result.read())
    result.close()
    print ("Auth Successful. The Auth ID Is:",response['result'])