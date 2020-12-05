# -*-coding:utf-8-*-
__author__ = 'hank'

import os
import json
import pandas as pd
import numpy as np
import akshare as ak
import sys
sys.path.append("../")
from lib.read_config import ReadConfig

class AnalysisData(object):
    def __init__(self):
        self.local = os.path.abspath('.')
        self.father_path = os.path.dirname(self.local)
        self.csv_path = self.father_path + "/resources/"

    def get_data_from_internet(self, code):
        '''获取数据并保存到csv'''

        # 获取原始数据
        original_data = ak.stock_zh_a_daily(symbol=code, adjust="qfq")
        # 取过去30天数据
        df = original_data.reset_index().iloc[:,:6]
        # 去除空值且从零开始编号索引
        df = df.dropna(how='any').reset_index(drop=True)
        # 按日期排序
        df = df.sort_values(by='date', ascending=True)

        # 均线数据
        df['10'] = df.close.rolling(10).mean()
        df['60'] = df.close.rolling(60).mean()
        df['250'] = df.close.rolling(250).mean()

        # 写入csv
        body_json = ReadConfig().read_json("code_list.json")
        first_dict = body_json["first_team"]
        second_dict = body_json["second_team"]
        if code in first_dict:
            file_name = self.csv_path + first_dict.get(code) + ".csv"
        elif code in second_dict:
            file_name = self.csv_path + second_dict.get(code) + ".csv"
        else:
            file_name = self.csv_path + code + ".csv"
        df.to_csv(file_name)

        return df

    def get_data_from_csv(self, code):
        '''从csv文件获取数据'''

        body_json = ReadConfig().read_json("code_list.json")
        first_dict = body_json["first_team"]
        second_dict = body_json["second_team"]
        if code in first_dict:
            file_name = self.csv_path + first_dict.get(code) + ".csv"
        elif code in second_dict:
            file_name = self.csv_path + second_dict.get(code) + ".csv"
        else:
            file_name = self.csv_path + code + ".csv"
        df = pd.read_csv(file_name, header=0)
        return df

if __name__ == "__main__":
    AnalysisData().get_data_from_internet("sh601318")
    AnalysisData().get_data_from_csv("sh601318")
