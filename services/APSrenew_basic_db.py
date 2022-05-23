import csv
import os

import pymongo
import baostock as bs
import pandas as pd

client = pymongo.MongoClient(host="localhost", port=27017)
db = client.stock
user = db.user
stock_all = db.stock_all  # 查询股票预测信息
stock_basic = db.stock_basic  # 查询股票基本信息
stock_daily = db.stock_daily  # 每日真实数据，包括换手率


# 每日更新基础数据库
def renew_basic_db():
    print("正在执行renew_basic_db的任务-------------------------------------------")
    path = "D:\\study\\code\\pycharmcode\\flaskProject\\services\\data\\stock_basic.csv"
    # path = "/usr/local/flaskProject/services/data/stock_basic.csv"  # linux
    print(path)
    if os.path.isfile(path):
        os.remove(path)
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
    result.to_csv(path, encoding="gbk", index=False)
    print(result)

    # 登出系统
    bs.logout()

    f = open(path, "r")
    reader = csv.DictReader(f)

    stock_basic.drop()
    stock_basic.insert_many(reader)


if __name__ == "__main__":
    renew_basic_db()
