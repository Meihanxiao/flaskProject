import baostock as bs
import pandas as pd

def avg(stock_code: str = "sh.603712", day: int = 30, target: list = [35, 39.58]) -> None:

    length = len(target)
    assert length <= 2, "长度必须小于2"
    
    res = []
    #### 登陆系统 ####
    lg = bs.login()
    # 显示登陆返回信息
    print('login respond error_code:'+lg.error_code)
    print('login respond  error_msg:'+lg.error_msg)

    rs = bs.query_history_k_data_plus(stock_code,
        "date,code,open,high,low,close",
        start_date='2021-12-20',
        frequency="d", adjustflag="2")
    print('query_history_k_data_plus respond error_code:'+rs.error_code)
    print('query_history_k_data_plus respond  error_msg:'+rs.error_msg)

    #### 打印结果集 ####
    data_list = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        data_list.append(rs.get_row_data())
    # print(data_list)
    # data_list.append(['2022-02-25',0,0,0,0,'29.01'])
    lendata = len(data_list)
    idx = 0
    sum30 = 0
    for i in range(1, day+1):
        print(data_list[-i])
        sum30 += float(data_list[-i][-1])
        idx+=1
    print(idx)
    res.append(sum30/day)
    if length == 1:
        left = target[0] * day - (sum30 - float(data_list[-(day) ][-1]))
        res.append(left)
    else:
        left = target[0] * day - (sum30 - float(data_list[-(day) ][-1]))
        right = target[1] * day - (sum30 - float(data_list[-(day) ][-1]))
        res.append(left)
        res.append(right)

    print(sum30, target[0] * day , left)
    #### 登出系统 ####
    bs.logout()
    
    return res

