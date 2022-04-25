import sys
import os
from configparser import ConfigParser
#sys.path.append(os.getcwd() + "\..")
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
import baostock as bs
from pathlib import Path

from script.down_model import get_down_stock_data

def test_for_get_down_stock_data():
    lg = bs.login()
    # 显示登陆返回信息
    print('login respond error_code:' + lg.error_code)
    print('login respond  error_msg:' + lg.error_msg)
    stock_dir = Path(__file__).parent / "../stock_industry.txt"
    stock_code_list = []

    with open(stock_dir, "r", encoding="utf-8") as fi:
        readlines = fi.readlines()
        for line in readlines:
            line = line.split(',')
            if line[3] != '' and (not line[2].startswith ("S") )and len(
                    line[1]) == 9 and (not line[2].startswith ("*")):
            #增加了   (not line[2].startswith ("*")) 条件
                stock_code_list.append(line[1])

    # stock_code_list = ["sh.603712"]
    print(len(stock_code_list))
    save_path = Path(__file__).parent / "../data/down_model7.txt"
    get_down_stock_data(lg, stock_code_list, save_path, sample_times=1000)
    bs.logout()


def data_validation():
    save_path = Path(__file__).parent / "../data/down_model7.txt"
    with open(save_path, "r", encoding="utf-8") as f:
        readlines = f.readlines()
        line_num = 0
        config_path = Path(__file__).parent / "../config.ini"
        parse = ConfigParser()
        parse.read(config_path, encoding="utf-8")
        DAY = int(parse.get("downtrain", "DAY"))
        WEEK = int(parse.get("downtrain", "WEEK"))
        MONTH = int(parse.get("downtrain", "MONTH"))
        flag=1
        for line in readlines:
            if line_num == 0:
                line_num += 1
                continue
            data_flag = 1
            line = line.split(',')
            if len(line[0]) != 9 or (not line[0].startswith ("sz")
                                     and not line[0].startswith ("sh")):
                data_flag = 0
            if line[1][4] != "-" or line[1][7] != "-":
                data_flag = 0
            if len(line)!= (DAY + WEEK + MONTH)*7+3:
                data_flag=0
            line_num += 1
            if 1-data_flag:
                flag=0
        if flag:
            print("test success")
        else:
            print("test fail")


if __name__ == "__main__":
    test_for_get_down_stock_data()
    data_validation()
