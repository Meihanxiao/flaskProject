import os
import sys
from configparser import ConfigParser

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
import baostock as bs
from pathlib import Path
from model.script.single_stock_up_model import get_single_stock_up_data

#stock_code_list = []


def test_for_get_single_stock_up_data(code) -> list:
    """
    test for single_stock_up_model, this function mainly downloads the data for each stock_all separately.

    """
    lg = bs.login()
    print('login respond error_code:' + lg.error_code)
    print('login respond  error_msg:' + lg.error_msg)
    """
    stock_dir = Path(__file__).parent / "../stock_industry.txt"
    debug = 1
    debug_idx = 0
    with open(stock_dir, "r", encoding="utf-8") as fi:
        readlines = fi.readlines()
        idx = 0
        for line in readlines:
            line = line.split(',')
            if line[3] != '' and (not line[2].startswith("S")) and len(
                    line[1]) == 9 and (not line[2].startswith("*")):
                #增加了   (not line[2].startswith ("*")) 条件
                stock_code_list.append(line[1])

            if debug:
                debug_idx += 1
                if debug_idx < 5:
                    print(line)
    """
    stock_code_list = code
    # print(len(stock_code_list))
    for stock_code in stock_code_list:
        file_path = stock_code + ".txt"
        save_path = Path(__file__).parent / "../data/up" / file_path
        """    
        save_dir_path = Path(__file__).parent / "../data/up"
        if not os.path.exists(save_dir_path):
            os.makedirs(save_dir_path)
        """
        print(save_path)
        flag_success = get_single_stock_up_data(lg, stock_code, save_path)
        if flag_success == 0:
            os.remove(save_path)

    bs.logout()

    #增加本次的股票代码列表


def data_validation():
    # TBD
    # 需要校验产生的数据是否符合原先的设计
    config_path = Path(__file__).parent / "../config.ini"
    parse = ConfigParser()
    parse.read(config_path, encoding="utf-8")
    DAY = int(parse.get("uptrain", "DAY"))
    WEEK = int(parse.get("uptrain", "WEEK"))
    MONTH = int(parse.get("uptrain", "MONTH"))
    flag=1
    save_path = Path(__file__).parent / "../data/up" / "sh.600000.txt"
    with open(save_path, "r", encoding="utf-8") as f:
        readlines=f.readlines()
        line_num =0
        for line in readlines:
            if line_num==0:
                line_num+=1
                continue
            data_flag=1
            line = line.split(',')
            if len(line[0]) != 9 or (not line[0].startswith ("sz")
                                     and not line[0].startswith ("sh")):
                data_flag = 0
            if int(line[1])!=line_num:
                data_flag=0
            if line[2][4] != "-" or line[2][7] != "-":
                data_flag = 0
            if len(line)!=(DAY + WEEK + MONTH)*7+4:
                data_flag=0
            line_num += 1
            if data_flag!=1:
                flag=0
    if flag:
        print("test success")
    else:
        print("test fail")


if __name__ == "__main__":
    test_for_get_single_stock_up_data()
    data_validation()
