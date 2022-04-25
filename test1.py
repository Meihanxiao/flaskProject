import datetime
import os

import pymongo
from flask import Flask
from flask_apscheduler import APScheduler
import baostock as bs
# 每日更新基础数据库
from model.algo.up.reg.RandomForest.eval_up import test_eval
from model.algo.up.reg.RandomForest.train_up import train_up
from model.common.eval import test_data_set_y, prediction_y
from model.tests.script_single_stock_up_model import test_for_get_single_stock_up_data
from services.txt_op import lines

def test1():
    file = open("D:/study/code/pycharmcode/flaskProject/model/data/up/test.txt", 'w').close()  # 清除test.txt
    with open(file="D:/study/code/pycharmcode/flaskProject/model/data/up/test.txt", mode="w") as f1:
        f1.write("invesment_id,date_id,target,f_0,f_1,f_2,f_3,f_4,f_5,f_6,f_7,f_8,f_9,f_10,f_11,f_12,f_13,f_14,f_15,"
                 "f_16,f_17,f_18,f_19,f_20,f_21,f_22,f_23,f_24,f_25,f_26,f_27,f_28,f_29,f_30,f_31,f_32,f_33,f_34,"
                 "f_35,f_36,f_37,f_38,f_39,f_40,f_41,f_42,f_43,f_44,f_45,f_46,f_47,f_48,f_49,f_50,f_51,f_52,f_53,"
                 "f_54,f_55,f_56,f_57,f_58,f_59,f_60,f_61,f_62,f_63,f_64,f_65,f_66,f_67,f_68,f_69,f_70,f_71,f_72,"
                 "f_73,f_74,f_75,f_76,f_77,f_78,f_79,f_80,f_81,f_82,f_83,f_84,f_85,f_86,f_87,f_88,f_89,f_90,f_91,"
                 "f_92,f_93,f_94,f_95,f_96,f_97,f_98,f_99,f_100,f_101,f_102,f_103,f_104,f_105,f_106,f_107,f_108,"
                 "f_109,f_110,f_111,f_112,f_113,f_114,f_115,f_116,f_117,f_118,f_119,f_120,f_121,f_122,f_123,f_124,"
                 "f_125,f_126,f_127,f_128,f_129,f_130,f_131,f_132,f_133,f_134,f_135,f_136,f_137,f_138,f_139" + "\r")
    file_list = []
    file_path = "D:/study/code/pycharmcode/flaskProject/model/data/up"
    image_dir_list = os.listdir(file_path)
    for file in image_dir_list:
        if os.path.basename(file)[0:2] == 'sh' or os.path.basename(file)[0:2] == 'sz':
            file_list.append(file)
    lines(file_list)


if __name__ == "__main__":
    test1()