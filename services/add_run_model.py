import os
import pymongo
import datetime
from model.algo.up.reg.RandomForest.eval_up import test_eval
import model.common.eval as eval
from model.algo.up.reg.RandomForest.train_up import train_up
from model.tests.script_single_stock_up_model import test_for_get_single_stock_up_data
from services.txt_op import lines


client = pymongo.MongoClient(host="localhost", port=27017)
db = client.stock
user = db.user
stock_all = db.stock_all  # 查询股票预测信息
stock_basic = db.stock_basic  # 查询股票基本信息
stock_daily = db.stock_daily  # 每日真实数据，包括换手率


# 定义任务执行程序（运行模型任务）
def add_run_model(codes):
    # 生成sh.txt
    test_for_get_single_stock_up_data(codes[0])
    print("生成.txt成功！！！")
    # 训练
    train_up(n=100)
    # print("数据训练成功！！！")
    # 更新test.txt
    file_list = [codes[0]+".txt"]
    lines(file_list)
    print("更新test.txt成功！！！")
    # 测试
    test_eval()
    print("数据测试成功！！！")
    # 更新到数据库
    temp = 0
    print(eval.test_data_set_y[0])
    for code in codes:
        result = stock_all.find_one({"stock_id": code})
        new_record = {"date": (datetime.datetime.now()).strftime("%Y-%m-%d"),
                      "stock_daily_predict_up": eval.test_data_set_y[temp],
                      "stock_daily_real_up": eval.prediction_y[temp], "stock_daily_predict_down": 0,
                      "stock_daily_real_down": 0}
        print(new_record)
        result['stock_data'].append(new_record)
        print(result['stock_data'])
        stock_all.update_one({'stock_id': code}, {'$set': result})
        temp = temp + 1


if __name__ == "__main__":
    add_run_model()
