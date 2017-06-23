# -*- coding: utf-8 -*-
###
# author: gefire@qq.com
###
import requests
import json


class SaltApi():
    def __init__(self, host, username, password, auth="pam"):
        self.salt_api_host = host
        self.username = username
        self.passoword = password
        self.auth = auth
        self.headers = {
            "Accept": "application/json",
            "Content-type": "application/json"
        }
        self.post_data = ""

    def do_post(self, api="login"):
        post_req = requests.post("%s/%s" % (self.salt_api_host, api), data=json.dumps(self.post_data),
                                 headers=self.headers)
        return post_req.json()["return"][0]

    def login(self):
        self.post_data = {
            "username": self.username,
            "password": self.passoword,
            "eauth": self.auth
        }
        resp = self.do_post()
        self.token = resp["token"]
        self.expire = resp["expire"]
        return self.token

    def run(self, fun="test.ping", target="*", arg_list=[]):
        self.post_data = [
            {
                "client": "local",
                "tgt": target,
                "fun": fun,
                "arg": arg_list,
                "username": self.username,
                "password": self.passoword,
                "eauth": self.auth
            }
        ]
        return self.do_post("run")
