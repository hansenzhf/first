# -*-coding:utf-8-*-
__author__ = 'hank'

import os
import json

class ReadConfig(object):
    def __init__(self):
        self.local = os.path.abspath('.')
        self.father_path = os.path.dirname(self.local)
        self.json_path = self.father_path + "/config/"

    def read_json(self, json_name):
        json_name = self.json_path + json_name
        with open(json_name, "r", encoding='utf8', errors='ignore') as f:
            body_json = json.load(f)
        return body_json