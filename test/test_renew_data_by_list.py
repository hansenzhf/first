# -*- coding: utf-8 -*-
__author__ = "hank"

import unittest
import sys
sys.path.append("../")
from lib.analysis_data import AnalysisData
from lib.read_config import ReadConfig

body_json = ReadConfig().read_json("code_list.json")
first_dict = body_json["first_team"]
second_dict = body_json["second_team"]
first_dict.update(second_dict)
print(first_dict)

class TestRenewDataByList(unittest.TestCase):
    def test_renew_data_by_list(self):
        '''按照list中对象更新数据'''

        for code in first_dict:
            name = first_dict.get(code)
            print("开始更新数据：<" + name + ">")
            try:
                AnalysisData().get_data_from_internet(code)
                print("<" + name + ">完成数据更新.")
            except Exception as e:
                print("<" + name + ">更新失败，原因是：" + e)
                continue

        print("所有数据更新完成.")

if __name__ == "__main__":
    TestRenewDataByList().test_renew_data_by_list()