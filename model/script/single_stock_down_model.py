import baostock as bs
import os 
from configparser import ConfigParser
from pathlib import Path 
import time

def get_single_stock_down_data(lg: bs, stock_code: list, save_path: str) -> None:

    config_path = Path(__file__).parent / "../config.ini"
    assert os.path.exists(config_path) == True 
    parse = ConfigParser()
    parse.read(config_path, encoding="utf-8")

    DAY = int(parse.get("downtrain", "DAY"))
    WEEK = int(parse.get("downtrain", "WEEK"))
    MONTH = int(parse.get("downtrain", "MONTH"))
    Prediction_day = int(parse.get("algorithm", "PREDICTION_DOWN_DAY"))
    
    with open(save_path, "w", encoding="utf-8") as f:
        f_num = (DAY+WEEK+MONTH)*7
        f.write("invesment_id,time_id,date_id,target")
        for i in range(f_num):
            f.write(",f_" + str(i))
        f.write("\n")

        # 天周月线指标：date,code,open,high,low,close,volume,amount,turn,pctChg
        # ----------------------------------------------------------------------
        rs = bs.query_history_k_data_plus(stock_code,
            "date,code,open,high,low,close,volume,turn, pctChg",
             end_date = time.strftime("%Y-%m-%d", time.localtime()),
            frequency="d", adjustflag="2")

        data_list_d = []
        while (rs.error_code == '0') & rs.next():
            data_list_d.append(rs.get_row_data())
        
        if len(data_list_d) < 60:
            return 0
        time_id = 0
        for idx in range(50, len(data_list_d)-10):
           
            date_endpoint = data_list_d[idx][0]  # 选取的时间点
            
            write_data = []
            write_flag = 1  # 表示需要正常写入，股票数据没有停牌之类的，也就是没有一个特征是0
            for i in range(idx, idx-DAY, -1):
                for k in range(2, len( data_list_d[i] )):
                    if data_list_d[i][k] == '' or float(data_list_d[i][k]) == 0:
                        write_flag = 0
                    if write_flag:
                        write_data.append(data_list_d[i][k])

            # ----------------------------------------------------------------------
            rs = bs.query_history_k_data_plus(stock_code,
                "date,code,open,high,low,close,volume,turn, pctChg",
                end_date=date_endpoint,
                frequency="w", adjustflag="2")
            data_list_w = []
            while (rs.error_code == '0') & rs.next():
                data_list_w.append(rs.get_row_data())

            if len(data_list_w) < 10:
                continue
            for i in range(-1, -1-WEEK, -1):
                for k in range(2, len( data_list_w[i] )):
                    # ['2018-07-31', 'sh.600000', '8.2740', '8.930900', '7.9400', '8.900', '43268988', '1.5409', '7.508']
                    if  data_list_w[i][k] == '' or float(data_list_w[i][k]) == 0:
                        write_flag = 0
                    if write_flag:
                        write_data.append(data_list_w[i][k])
            # ----------------------------------------------------------------------
            rs = bs.query_history_k_data_plus(stock_code,
                "date,code,open,high,low,close,volume,turn, pctChg",
                end_date=date_endpoint,
                frequency="m", adjustflag="2")
            data_list_m = []
            while (rs.error_code == '0') & rs.next():
                data_list_m.append(rs.get_row_data())
            if len(data_list_m) < 5:
                continue
            for i in range(-1, -1-MONTH, -1):
                for k in range(2, len( data_list_m[i] )):
                    if data_list_m[i][k] == '' or float(data_list_m[i][k]) == 0:
                        write_flag = 0
                    if write_flag:
                        write_data.append(data_list_m[i][k])
            # =====================================================================
            if write_flag:
                # get the prediction value_y, 2-open, 5-close, value_y = (close - open)/open
                min_close = 99999.
                for i in range(idx+1, idx+1+Prediction_day):
                    min_close = min(min_close, float(data_list_d[i][5]))         
                value_y_tmp = (min_close - float(data_list_d[idx+1][2])) / float(data_list_d[idx+1][2])
            
            # =====================================================================
            # print(write_flag)
            if write_flag and len(write_data) == f_num:
                time_id += 1
                f.write(stock_code + "," + str(time_id) + "," + date_endpoint)
                if time_id % 20 ==0:
                    print("write into...", time_id, len(data_list_d))
                    print(date_endpoint, stock_code)
                f.write("," + str(  round(float(value_y_tmp), 4) ) )
                # print(str(  round(float(value_y_tmp), 4) ))
                assert_idx = 0
                for i in range(len(write_data)):
                    f.write(','+ str( round(float(write_data[i]),2) ) )
                    assert_idx += 1
                
                if assert_idx != f_num:
                    print("wrong, ", assert_idx, stock_code, date_endpoint )

                f.write("\n")
