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


def cs():
    path = os.path.dirname(os.getcwd())
    # WinPate =
    LinuxPath = path + "/app.py"
    print(LinuxPath)


if __name__ == "__main__":
    cs()
