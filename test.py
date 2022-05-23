import datetime
import os
import csv
import pymongo
from flask import Flask
from flask_apscheduler import APScheduler
import baostock as bs
from dateutil.relativedelta import relativedelta
import pandas as pd
# 每日更新基础数据库
from model.algo.up.reg.RandomForest.eval_up import test_eval
from model.algo.up.reg.RandomForest.train_up import train_up
import model.common.eval as eval
from model.tests.script_single_stock_up_model import test_for_get_single_stock_up_data
from services.txt_op import lines


client = pymongo.MongoClient(host="localhost", port=27017)
db = client.stock
user = db.user
stock_all = db.stock_all  # 查询股票预测信息
stock_basic = db.stock_basic  # 查询股票基本信息
stock_daily = db.stock_daily  # 每日真实数据，包括换手率


def test():
    import baostock as bs
    import pandas as pd

    # 登陆系统
    lg = bs.login()
    # 显示登陆返回信息
    print('login respond error_code:' + lg.error_code)
    print('login respond  error_msg:' + lg.error_msg)

    # 获取证券基本资料
    rs = bs.query_stock_basic()
    # rs = bs.query_stock_basic(code_name="浦发银行")  # 支持模糊查询
    print('query_stock_basic respond error_code:' + rs.error_code)
    print('query_stock_basic respond  error_msg:' + rs.error_msg)

    # 打印结果集
    data_list = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        data_list.append(rs.get_row_data())
    result = pd.DataFrame(data_list, columns=rs.fields)
    # 结果集输出到csv文件
    result.to_csv("D:/stock_basic.csv", encoding="gbk", index=False)
    print(result)

    # 登出系统
    bs.logout()

if __name__ == "__main__":
    test()
