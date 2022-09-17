'''
Descripttion: Automatically generated file comment
version: 
Author: Wesley
Date: 2021-02-22 16:25:48
LastEditors: Wesley
LastEditTime: 2021-08-25 14:20:57
'''
from datetime import date
from wtpy.apps.datahelper import DHFactory as DHF

# tushare
hlper = DHF.createHelper("tushare")
hlper.auth(**{"token":"babe101c6d980a895d0d697efa3ca25477e205bd1b16076e3da7ee92", "use_pro":True})
# hlper = DHF.createHelper("baostock")
# hlper.auth()

# 下载K线数据
# hlper.dmpBarsToFile(folder='./', codes=["CFFEX.IF.HOT","CFFEX.IC.HOT"], period='min1')
# hlper.dmpBarsToFile(folder='./', codes=["CFFEX.IF.HOT","CFFEX.IC.HOT"], period='day')
# hlper.dmpBarsToFile(folder='./', codes=["ZCE.CF301"], period='day', start_date=date(2022,9,14), end_date=date(2022,9,16))
# hlper.dmpBarsToFile(folder='./', codes=["CZCE.SR.HOT"], period='day', start_date=date(2022,9,14), end_date=date(2022,9,16))
hlper.dmpBarsToFile(folder='./', codes=["CFFEX.IF.2303"], period='day')
# hlper.dmpBarsToFile(folder='./', codes=["SZSE.399005"], period='min5', start_date=date(2022,9,14), end_date=date(2022,9,16))
# hlper.dmpBarsToFile(folder='./', codes=["SZSE.399005","SZSE.399006","SZSE.399303"], period='day')