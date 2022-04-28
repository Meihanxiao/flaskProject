import csv
import datetime
import os

import pymongo
import baostock as bs
import pandas as pd
from dateutil.relativedelta import relativedelta

client = pymongo.MongoClient(host="localhost", port=27017)
db = client.stock
user = db.user
stock_all = db.stock_all  # 查询股票预测信息
stock_basic = db.stock_basic  # 查询股票基本信息
stock_daily = db.stock_daily  # 每日真实数据，包括换手率


def renew_daily_db():
    today = (datetime.datetime.now()).strftime("%Y-%m-%d")
    if stock_daily.find({"date": today}):
        pass
    else:
        print("正在执行renew_daily_db的任务-------------------------------------------")
        # path = os.path.dirname(__file__) + "\data\history_A_stock_k_data.csv"
        # path = os.path.dirname(__file__) + "/data/history_A_stock_k_data.csv"
        path = "D:\\study\\code\\pycharmcode\\flaskProject\\services\\data\\history_A_stock_k_data.csv"
        # path = "/usr/local/flaskProject/services/data/history_A_stock_k_data.csv"
        if os.path.isfile(path):
            os.remove(path)
        code_list = []

        name_condition = {"$or": [{"stock_id": {'$regex': '^sh.6'}}, {"stock_id": {'$regex': '^sz.00'}},
                                  {"stock_id": {'$regex': '^sz.30'}}]}
        new_data = db.stock_all.find(name_condition)
        for data in new_data:
            code_list.append(data['stock_id'])

        data_list = []

        # 登陆系统
        lg = bs.login()
        now_time = datetime.datetime.now().strftime("%Y-%m-%d")
        yesterday = (datetime.datetime.now() + relativedelta(days=-1)).strftime("%Y-%m-%d")
        print(now_time)
        print(yesterday)
        for code in code_list:
            print(code)
            rs = bs.query_history_k_data_plus(code,
                                              "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,isST",
                                              start_date=now_time, end_date=now_time,
                                              frequency="d", adjustflag="3")
            # 打印结果集
            while (rs.error_code == '0') & rs.next():
                # 获取一条记录，将记录合并在一起
                data_list.append(rs.get_row_data())
        result = pd.DataFrame(data_list, columns=rs.fields)
        # 结果集输出到csv文件
        result.to_csv(path, index=False)
        print(result)

        # 登出系统
        bs.logout()
        f = open(path, "r")
        reader = csv.DictReader(f)

        stock_daily.drop()
        stock_daily.insert_many(reader)


if __name__ == "__main__":
    renew_daily_db()
