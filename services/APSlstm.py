import datetime

import pymongo
from baostock import query_trade_dates
import baostock as bs
from model.run import run_model

client = pymongo.MongoClient(host="localhost", port=27017)
db = client.stock
user = db.user
stock_all = db.stock_all  # 查询股票预测信息
stock_basic = db.stock_basic  # 查询股票基本信息
stock_daily = db.stock_daily  # 每日真实数据，包括换手率
today = (datetime.datetime.now()).strftime("%Y-%m-%d")


def run_lstm():
    lg = bs.login()
    flag = query_trade_dates(start_date=today, end_date=today).get_row_data()[1]
    flag1 = stock_all.find_one({'stock_id': "sh.600000"})["stock_data"][-1]["date"]
    if stock_daily.find({"date": today}) and flag == "1" and flag1 != today:
        print("正在执行run_model的任务-------------------------------------------")
        # 获得被选中的股票
        code_list = []
        results = stock_all.find({'if_choose': {'$gt': 0}})
        for result in results:
            code_list.append(result['stock_id'])
            print("选择的股票有：" + result['stock_id'])
        # code_list = ["sh.600000"]
        for code in code_list:
            new_code = code.split(".")[1] + "." +code.split(".")[0].upper()
            print(new_code)
            actual_stock_open, predicted_stock_open, actual_stock_close, predicted_stock_close = run_model(new_code)
            print(actual_stock_open[-1][0], predicted_stock_open[-1][0], actual_stock_close[-1][0], predicted_stock_close[-1][0])
            new_record = {"date": datetime.datetime.now().strftime("%Y-%m-%d"),
                          "stock_daily_predict_up": round(float(predicted_stock_open[-1][0]), 2),
                          "stock_daily_real_up": round(float(actual_stock_open[-1][0]), 2),
                          "stock_daily_predict_down": round(float(predicted_stock_close[-1][0]), 2),
                          "stock_daily_real_down": round(float(actual_stock_close[-1][0]), 2)}
            print(new_record)
            result = stock_all.find_one({"stock_id": code})
            result['stock_data'].append(new_record)
            print(result)
            stock_all.update_one({"stock_id":code}, {'$set': result})
    else:
        pass


if __name__ == "__main__":
    run_lstm()