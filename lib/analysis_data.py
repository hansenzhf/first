# -*-coding:utf-8-*-
__author__ = 'hank'

import os
import pandas as pd
import numpy as np
import akshare as ak

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
        df['5'] = df.close.rolling(5).mean()
        df['10'] = df.close.rolling(10).mean()

        # 写入csv
        file_name = self.csv_path + code + ".csv"
        df.to_csv(file_name)

        return df

    def get_data_from_csv(self, code):
        '''从csv文件获取数据'''

        file_name = self.csv_path + code + ".csv"
        df = pd.read_csv(file_name, header=0)
        print(df.tail())

if __name__ == "__main__":
    AnalysisData().get_data_from_internet("sh601318")
    AnalysisData().get_data_from_csv("sh601318")
