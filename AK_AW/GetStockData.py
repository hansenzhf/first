# coding=uft-8
author = 'hank'

import pandas as pd
import numpy as np
import akshare as ak

class GetStockData(object):
    def get_price_data(self, code):
        pingan = ak.stock_zh_a_daily(symbol="sh601318", adjust="qfq")
        df3 = pingan.reset_index().iloc[-30:,:6]  #取过去30天数据
        df3 = df3.dropna(how='any').reset_index(drop=True) #去除空值且从零开始编号索引
        df3 = df3.sort_values(by='date', ascending=True)
        print(df3.info())

        # 均线数据
        df3['5'] = df3.close.rolling(5).mean()
        df3['10'] = df3.close.rolling(10).mean()

        df3.tail()
