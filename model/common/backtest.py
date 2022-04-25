import imp
import sys
import os
import json
import pandas as pd
import numpy as np
import pickle
from pathlib import Path
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
import baostock as bs
from pathlib import Path
from script.down_model import get_down_stock_data
from script.single_stock_down_model import get_single_stock_down_data
from script.single_stock_up_model import get_single_stock_up_data
from script.up_model import get_all_stock_data
from common.datasets import read_down_dataset
from common.datasets import read_up_dataset
from common.metrics import calculate_acc
from common.metrics import calculate_evs
from common.metrics import calculate_f1
from common.metrics import calculate_mae
from common.metrics import calculate_medae
from common.metrics import calculate_mse
from common.metrics import calculate_precision
from common.metrics import calculate_r2
from common.metrics import calculate_recall
from common.datasets import read_up_single_stock_dataset
from common.datasets import read_down_single_stock_dataset

def backtest(
            stock_list:list = ["sz.000001"],
            start_date:str = "2000-01-01",
            end_date:str = "2022-01-14",
            sample_times:int = 1000,
            type_sample:str = 'times',
            type:str = 'reg',
            type_ud:str = 'up',
            model_save_path = Path(__file__).parent / "../algo/cla/svm/save_model/toy_up_model.pickle",
            save_path: str = Path(__file__).parent / "../data/backset/down_model.txt",
            classification_threshold: list = [0,0.05],
            save_md_path:str = Path(__file__).parent / "../data/backtest/output/metr.md" ,
            save_json_path: str = Path(__file__).parent / "../data/backtest/output/metri.json" ,
            ):


    lg = bs.login()
        # 显示登陆返回信息
    print('login respond error_code:' + lg.error_code)
    print('login respond  error_msg:' + lg.error_msg)
    if type_sample == 'times':
        if type_ud == 'down':
            get_down_stock_data(lg, stock_list, save_path, sample_times)
        else :
            get_all_stock_data(lg, stock_list, save_path, sample_times)
        bs.logout()
        if type == 'reg':
            if type_ud =='down':
                data_set_x, data_set_reg_y = read_down_dataset(path = save_path, type = type)
            else :
                data_set_x, data_set_reg_y = read_up_dataset(path = save_path, type = type)
            with open(model_save_path, 'rb') as f:  
                clf_load = pickle.load(f)
                model_reg_y = clf_load.predict(data_set_x) 
            metrics = pd.DataFrame({'Explained variance score': calculate_evs(data_set_reg_y, model_reg_y),
                                    'Mean absolute error': calculate_mae(data_set_reg_y, model_reg_y),
                                    'Mean squared error': calculate_mse(data_set_reg_y, model_reg_y),
                                    'Median absolute error': calculate_medae(data_set_reg_y, model_reg_y),
                                    'R2': calculate_r2(data_set_reg_y, model_reg_y)},index=[0])
            with open(save_md_path, "w",encoding="utf-8") as fw:
                fw.write(metrics.head().to_markdown())
            with open(save_json_path, "w", encoding="utf-8") as f:
                f.write(mdtojson(metrics.head().to_markdown()))


        else:
            if type_ud=='down':
                data_set_x, data_set_cla_y = read_down_dataset(save_path,classification_threshold,type)
            else :
                data_set_x, data_set_cla_y = read_up_dataset(save_path,classification_threshold,type)
            with open(model_save_path, 'rb') as f:  
                clf_load = pickle.load(f)
                model_cla_y = clf_load.predict(data_set_x) 
            model_cla_y = model_cla_y.astype(np.uint8)
            metrics = pd.DataFrame({'accuracy_score': calculate_acc(data_set_cla_y, model_cla_y),
                                    'recall': calculate_recall(data_set_cla_y, model_cla_y),
                                    'precision': calculate_precision(data_set_cla_y, model_cla_y),
                                    'F1-score': calculate_f1(data_set_cla_y, model_cla_y)},index=[0])
            with open(save_md_path, "w",encoding="utf-8") as fw:
                fw.write(metrics.head().to_markdown())
            with open(save_json_path, "w", encoding="utf-8") as f:
                f.write(mdtojson(metrics.head().to_markdown()))
       
    else :       
        for stock_code in stock_list:
            file_path = stock_code + ".txt"
            save_path_now = Path(__file__).parent / "../data/down/backset" / file_path
            if type_ud == 'down':
                get_single_stock_down_data(lg, stock_code, save_path_now, start_date, end_date)
            else :
                get_single_stock_up_data(lg, stock_code, save_path_now, start_date, end_date)
        bs.logout()
        with open(save_path, "w", encoding="utf-8") as fw:
            for stock_code in stock_list: 
                if stock_code == stock_list[0]:
                    flag = 1
                else :
                    flag = 0
                file_path = stock_code + ".txt"
                save_path_now = Path(__file__).parent / "../data/down/backset" / file_path

                with open(save_path_now, "r", encoding="utf-8") as fr:
                    readlines = fr.readlines()
                    line_num = 0
                    for line in readlines:
                        if line_num == 0 and flag == 0:
                            line_num += 1
                            continue
                        fw.write(line)                            
        
        if type=="reg":
            if type_ud == 'up':
                data_set_x, data_set_reg_y = read_up_single_stock_dataset(path=save_path,type = type) 
            else :
                data_set_x,data_set_reg_y = read_down_single_stock_dataset(path=save_path,type = type)
            with open(model_save_path, 'rb') as f:  
                clf_load = pickle.load(f)
                model_reg_y = clf_load.predict(data_set_x)
            metrics = pd.DataFrame({'Explained variance score': calculate_evs(data_set_reg_y, model_reg_y),
                                    'Mean absolute error': calculate_mae(data_set_reg_y, model_reg_y),
                                    'Mean squared error': calculate_mse(data_set_reg_y, model_reg_y),
                                    'Median absolute error': calculate_medae(data_set_reg_y, model_reg_y),
                                    'R2': calculate_r2(data_set_reg_y, model_reg_y)},index=[0])
            with open(save_md_path, "w",encoding="utf-8") as fw:
                fw.write(metrics.head().to_markdown())
            with open(save_json_path, "w", encoding="utf-8") as f:
                f.write(mdtojson(metrics.head().to_markdown()))
        else :
            if type_ud == 'up':
                data_set_x, data_set_cla_y = read_up_single_stock_dataset(save_path,classification_threshold,type) 
            else :
                data_set_x, data_set_cla_y = read_up_single_stock_dataset(save_path,classification_threshold,type)
            with open(model_save_path, 'rb') as f:  
                clf_load = pickle.load(f)
                model_cla_y = clf_load.predict(data_set_x)
            model_cla_y = model_cla_y.astype(np.uint8)
            metrics = pd.DataFrame({'accuracy_score': calculate_acc(data_set_cla_y, model_cla_y),
                                    'recall': calculate_recall(data_set_cla_y, model_cla_y),
                                    'precision': calculate_precision(data_set_cla_y, model_cla_y),
                                    'F1-score': calculate_f1(data_set_cla_y, model_cla_y)},index=[0])
            with open(save_md_path, "w",encoding="utf-8") as fw:
                fw.write(metrics.head().to_markdown())
            with open(save_json_path, "w", encoding="utf-8") as f:
                f.write(mdtojson(metrics.head().to_markdown()))

def mdtojson(metrics):
    lines = metrics.split('\n')
    ret=[]
    keys=[]
    for i,l in enumerate(lines):
        if i==0:
            keys=[_i.strip() for _i in l.split('|')]
        elif i==1: continue
        else:
            ret.append({keys[_i]:v.strip() for _i,v in enumerate(l.split('|')) if  _i>0 and _i<len(keys)-1})
    return json.dumps(ret, indent = 4)