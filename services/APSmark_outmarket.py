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


def mark_outmarket():
    print("正在执行mark_outmarket的任务-------------------------------------------")
    code_list_in_all = []
    new_data = db.stock_all.find()
    for data in new_data:
        code_list_in_all.append(data['stock_id'])
    for code in code_list_in_all:
        # print(code)
        if stock_basic.find_one({"code": code}):
            if stock_basic.find_one({"code": code})['status'] == "0":
                result = stock_all.find_one({"stock_id": code})
                if result["stock_name"][-2] == "退":
                    pass
                else:
                    result["stock_name"] = result["stock_name"] + "（退）"
                stock_all.update_one({"stock_id": code}, {'$set': result})


if __name__ == "__main__":
    mark_outmarket()
