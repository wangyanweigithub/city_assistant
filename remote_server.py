import requests
import base64
import json
import hashlib
import datetime
from setting import Common

class Encrypt(object):

    @classmethod
    def gen_md(cls, params):
        md = hashlib.md5()
        md.update(params.encode("utf8"))
        return md.hexdigest()

    @classmethod
    def gen_base64(cls, params):
        return base64.b64encode(params.encode("utf8"))


class RemoteServer(object):
    def __init__(self, url):
        self.url = url

    @staticmethod
    def gen_params(account, passwd):
        time_now = datetime.datetime.now()
        time_str = time_now.strftime("%Y%m%d%H%M%S")
        param = {"username": account, "password": passwd, "date": time_str,
                 "key": Encrypt.gen_md("thd" + time_str + '321')}
        params_json = json.dumps(param)
        token = Encrypt.gen_base64(params_json)
        return token

    def login(self, account, passwd):
        token = self.gen_params(account, passwd)
        response = requests.post(self.url, {"token": token})
        response = response.json()
        if response['code'] == Common.login['success']:
            return True, response['message']
        return False, response['message']


def main():
    api = RemoteServer("http://mcenterv2.thd99.com/V2/pythonApi/sign")
    login_response = api.login("name", "123")
    status, message = login_response
    print(status, message)


if __name__ == "__main__":
    main()