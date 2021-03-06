# import win32com.client
# import pythoncom
# import os
# import sys
# import inspect
# import sqlite3
# from pandas import DataFrame, Series, Panel
# import matplotlib
# import matplotlib.pyplot as plt
from XingAPI import XingAPI
import pandas as pd

api = XingAPI()
account_path = pd.read_csv('private\\info.csv')
api.login(account_path)
accounts = api.getAccount()

# week_data1 = api.t1514_업종기간별추이(업종코드='001', 구분1='', 구분2='1', CTS일자='', 조회건수='10', 비중구분='')
# print(week_data1)

# test_data = api.t0424_주식잔고2(accounts[0], 0000, 1, 0, 0, 0, '')
# print(test_data)

test_data2 = api.t8412_주식차트N분(단축코드='005930', 분단위='1', 요청건수='2000',연속조회=True, cts_time='', cts_date='')
test_data2.to_csv('Stock.csv', index=False, mode='w',encoding='utf-8-sig')
# print(test_data2)

# data = api.t8436_주식종목조회(구분='0')
# data.to_csv('Stocks.csv', index=False, mode='w',encoding='utf-8-sig')