import os
import pymongo
import datetime

from dateutil.relativedelta import relativedelta

from model.algo.up.reg.RandomForest.eval_up import test_eval as eval_up
from model.algo.down.reg.RandomForest.eval_down import test_eval as eval_down
import model.common.eval as eval
from model.algo.up.reg.RandomForest.train_up import train_up
from model.algo.down.reg.RandomForest.train_down import train_down
from model.tests.script_single_stock_up_model import test_for_get_single_stock_up_data
from model.tests.script_single_stock_down_model import test_for_get_single_stock_down_data
from services.txt_op import lines, lines1

client = pymongo.MongoClient(host="localhost", port=27017)
db = client.stock
user = db.user
stock_all = db.stock_all  # 查询股票预测信息
stock_basic = db.stock_basic  # 查询股票基本信息
stock_daily = db.stock_daily  # 每日真实数据，包括换手率
global j
j = 1
# 定义任务执行程序（运行模型任务）
def run_model():
    global j
    today = (datetime.datetime.now()).strftime("%Y-%m-%d")
    if stock_daily.find({"date": today}) and j != 1:
        print("正在执行run_model的任务-------------------------------------------")
        # 获得被选中的股票
        code_lists = []
        results = stock_all.find({'if_choose': {'$gt': 0}})
        for result in results:
            code_lists.append(result['stock_id'])
            print("选择的股票有：" + result['stock_id'])
        # 生成sh.txt
        test_for_get_single_stock_up_data(code_lists)
        test_for_get_single_stock_down_data(code_lists)
        print("生成.txt成功！！！")




        # 训练
        train_up(n=100)
        print("数据训练成功！！！")

        # 更新test.txt
        path = "D:\\study\\code\\pycharmcode\\flaskProject\\model\\data\\up\\test.txt" # windows
        # path = "/usr/local/flaskProject/model/data/up/test.txt"  # linux



        file = open(path, 'w').close()  # 清除test.txt
        with open(file=path, mode="w") as f1:
            f1.write(
                "invesment_id,date_id,target,f_0,f_1,f_2,f_3,f_4,f_5,f_6,f_7,f_8,f_9,f_10,f_11,f_12,f_13,f_14,f_15,"
                "f_16,f_17,f_18,f_19,f_20,f_21,f_22,f_23,f_24,f_25,f_26,f_27,f_28,f_29,f_30,f_31,f_32,f_33,f_34,"
                "f_35,f_36,f_37,f_38,f_39,f_40,f_41,f_42,f_43,f_44,f_45,f_46,f_47,f_48,f_49,f_50,f_51,f_52,f_53,"
                "f_54,f_55,f_56,f_57,f_58,f_59,f_60,f_61,f_62,f_63,f_64,f_65,f_66,f_67,f_68,f_69,f_70,f_71,f_72,"
                "f_73,f_74,f_75,f_76,f_77,f_78,f_79,f_80,f_81,f_82,f_83,f_84,f_85,f_86,f_87,f_88,f_89,f_90,f_91,"
                "f_92,f_93,f_94,f_95,f_96,f_97,f_98,f_99,f_100,f_101,f_102,f_103,f_104,f_105,f_106,f_107,f_108,"
                "f_109,f_110,f_111,f_112,f_113,f_114,f_115,f_116,f_117,f_118,f_119,f_120,f_121,f_122,f_123,f_124,"
                "f_125,f_126,f_127,f_128,f_129,f_130,f_131,f_132,f_133,f_134,f_135,f_136,f_137,f_138,f_139" + "\r")
        file_list = []
        file_path = "D:\\study\\code\\pycharmcode\\flaskProject\\model\\data\\up"  # windows
        # file_path = "/usr/local/flaskProject/model/data/up"  # linux
        image_dir_list = os.listdir(file_path)
        for file in image_dir_list:
            if os.path.basename(file)[0:2] == 'sh' or os.path.basename(file)[0:2] == 'sz':
                file_list.append(file)
        lines(file_list)


        # 测试
        eval_up()
        print("数据测试成功！！！")
        stock_daily_predict_up = eval.test_data_set_y
        stock_daily_real_up = eval.prediction_y
        print("涨")
        print(stock_daily_predict_up)
        print(stock_daily_real_up)








        # 训练
        train_down(n=100)
        print("数据训练成功！！！")

        # 更新test.txt
        path = "D:\\study\\code\\pycharmcode\\flaskProject\\model\\data\\down\\test.txt"  # windows
        # path = "/usr/local/flaskProject/model/data/up/test.txt"  # linux

        file = open(path, 'w').close()  # 清除test.txt
        with open(file=path, mode="w") as f1:
            f1.write(
                "invesment_id,date_id,target,f_0,f_1,f_2,f_3,f_4,f_5,f_6,f_7,f_8,f_9,f_10,f_11,f_12,f_13,f_14,f_15,"
                "f_16,f_17,f_18,f_19,f_20,f_21,f_22,f_23,f_24,f_25,f_26,f_27,f_28,f_29,f_30,f_31,f_32,f_33,f_34,"
                "f_35,f_36,f_37,f_38,f_39,f_40,f_41,f_42,f_43,f_44,f_45,f_46,f_47,f_48,f_49,f_50,f_51,f_52,f_53,"
                "f_54,f_55,f_56,f_57,f_58,f_59,f_60,f_61,f_62,f_63,f_64,f_65,f_66,f_67,f_68,f_69,f_70,f_71,f_72,"
                "f_73,f_74,f_75,f_76,f_77,f_78,f_79,f_80,f_81,f_82,f_83,f_84,f_85,f_86,f_87,f_88,f_89,f_90,f_91,"
                "f_92,f_93,f_94,f_95,f_96,f_97,f_98,f_99,f_100,f_101,f_102,f_103,f_104,f_105,f_106,f_107,f_108,"
                "f_109,f_110,f_111,f_112,f_113,f_114,f_115,f_116,f_117,f_118,f_119,f_120,f_121,f_122,f_123,f_124,"
                "f_125,f_126,f_127,f_128,f_129,f_130,f_131,f_132,f_133,f_134,f_135,f_136,f_137,f_138,f_139" + "\r")
        file_list = []
        # file_path = path + "\model\data\up"
        file_path = "D:\\study\\code\\pycharmcode\\flaskProject\\model\\data\\down"  # windows
        # file_path = "/usr/local/flaskProject/model/data/up"  # linux
        image_dir_list = os.listdir(file_path)
        for file in image_dir_list:
            if os.path.basename(file)[0:2] == 'sh' or os.path.basename(file)[0:2] == 'sz':
                file_list.append(file)
        lines1(file_list)





        # 测试
        eval_down()
        print("数据测试成功！！！")
        stock_daily_predict_down = eval.test_data_set_y
        stock_daily_real_down = eval.prediction_y
        print("跌")
        print(stock_daily_predict_down)
        print(stock_daily_real_down)















        # 更新到数据库
        temp = 0
        for code in code_lists:
            result = stock_all.find_one({"stock_id": code})
            new_record = {"date": (datetime.datetime.now()).strftime("%Y-%m-%d"),
                          "stock_daily_predict_up": stock_daily_predict_up[temp],
                          "stock_daily_real_up": stock_daily_real_up[temp], "stock_daily_predict_down": stock_daily_predict_down[temp],
                          "stock_daily_real_down": stock_daily_real_down[temp]}
            print(new_record)
            result['stock_data'].append(new_record)
            print(result['stock_data'])
            stock_all.update_one({'stock_id': code}, {'$set': result})
            temp = temp + 1
        j = 1
        print("模型预测结束")

    elif stock_daily.find({"date": today}) and j == 1:
        pass
    elif not stock_daily.find({"date": today}):
        j = 0
        pass


if __name__ == "__main__":
    run_model()
