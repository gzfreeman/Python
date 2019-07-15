import requests
import json


def __init__(self):
    self.url = 'http://192.168.10.11/api_jsonrpc.php'
    self.headers = {'Content-Type': 'application/json'}
    auth = {
        "jsonrpc": "2.0",
        "method": "user.login",
        "params": {
            "user": "Admin",
            "password": "jnadmin123"
        },
        "id": 1,
        "auth": None,
    }
    response = requests.post(self.url, data=json.dumps(auth), headers=self.headers)
    authid = json.loads(response.text)['result']
    #print(authid)



    def get_hosts():
        content = {
            "jsonrpc": "2.0",
            "method": "host.get",
            "params": {
                "output": [
                    "hostid",
                    "host"
                ],
                "selectInterfaces": [
                    "interfaceid",
                    "ip"
                ]
            },
            "id": 2,
            "auth": authid
        }
        response = requests.post(self.url, data=json.dumps(content), headers=self.headers)
        print(response.text)

    if __name__ == '__main__':
        get_hosts