from cProfile import label
import pandas as pd
import numpy as np
from pathlib import Path 
import pickle
import os 
import sys
sys.path.append(os.getcwd())
from model.common.datasets import read_up_dataset
from model.common.datasets import read_down_dataset
from model.common.datasets import read_down_single_stock_dataset
from model.common.datasets import read_up_single_stock_dataset
from model.common.metrics import calculate_acc
from model.common.metrics import calculate_evs
from model.common.metrics import calculate_f1
from model.common.metrics import calculate_mae
from model.common.metrics import calculate_medae
from model.common.metrics import calculate_mse
from model.common.metrics import calculate_precision
from model.common.metrics import calculate_r2
from model.common.metrics import calculate_recall
#from data_processing import post_processing
from model.common.backtest import mdtojson
global test_data_set_y
global prediction_y
def eval_processing(
                test_path: str = Path(__file__).parent / "../data/toy_test_up_model_20_8_3.txt", 
                model_save_path: str = Path(__file__).parent / "../algo/reg/svm/save_model/toy_up_model.pickle",
                type:str = "cla",
                save_md_path:str = Path(__file__).parent / "../algo/reg/svm/output/metr.md" ,
                save_json_path: str = Path(__file__).parent / "../algo/reg/svm/output/metri.json" ,
                classification_threshold: list = [0,0.05],
                type_ud:str = "up",
                type_stock: str = "all"
                ):
    global test_data_set_y
    global prediction_y
    with open(model_save_path, 'rb') as f:  
        clf_load = pickle.load(f) 
        if type_ud == "up" and type_stock =="all":
            test_data_set_x, test_data_set_y = read_up_dataset(test_path, classification_threshold, type)
        elif type_ud == "up" and type_stock =="single":
            test_data_set_x, test_data_set_y = read_up_single_stock_dataset(test_path, classification_threshold, type)
        elif type_ud == "down" and type_stock == "all" :
            test_data_set_x, test_data_set_y = read_down_dataset(test_path, classification_threshold, type)
        else :
            test_data_set_x, test_data_set_y = read_down_single_stock_dataset(test_path, classification_threshold, type)
            
        """
        # post processing
        #test_data_set_x = post_processing(test_data_set_x)
        debug = 0
        if debug == 0:
            test_x, test_y = [], []
            label_num = []
            for i in range (len(classification_threshold)+2):
                label_num .append(75)
          #  print(label_num)

            for i in range(len(test_data_set_y)):
                if label_num[test_data_set_y[i]] >0:
                    label_num[test_data_set_y[i]]-=1
                    test_x.append(test_data_set_x[i])
                    test_y.append(test_data_set_y[i])
              
            test_data_set_x = np.array(test_x)
            test_data_set_y = np.array(test_y)

        if debug==1:
            print(test_data_set_y)
            stat = {}
            for item in test_data_set_y:
                if item not in stat:
                    stat[item] = 1
                else:
                    stat[item] += 1
            print(stat)
        """

        prediction_y = clf_load.predict(test_data_set_x)
        prediction_y = np.array(prediction_y)
    #    print(clf_load.predict_proba(test_data_set_x) )
        print("test_data_set_y: ", test_data_set_y)
        print("prediciton: ", prediction_y)
        
        if type=="reg":

            metrics = pd.DataFrame({'Explained variance score': calculate_evs(test_data_set_y, prediction_y),
                                    'Mean absolute error': calculate_mae(test_data_set_y, prediction_y),
                                    'Mean squared error': calculate_mse(test_data_set_y, prediction_y),
                                    'Median absolute error': calculate_medae(test_data_set_y, prediction_y),
                                    'R2': calculate_r2(test_data_set_y, prediction_y)},index=[0])

            with open(save_md_path, "w",encoding="utf-8") as fw:
                fw.write(metrics.head().to_markdown())
            with open(save_json_path, "w", encoding="utf-8") as f:
                f.write(mdtojson(metrics.head().to_markdown()))
        else :
            prediction_y = prediction_y.astype(np.uint8)
            metrics = pd.DataFrame({'accuracy_score': calculate_acc(test_data_set_y, prediction_y),
                                    'recall': calculate_recall(test_data_set_y, prediction_y),
                                    'precision': calculate_precision(test_data_set_y, prediction_y),
                                    'F1-score': calculate_f1(test_data_set_y, prediction_y)},index=[0])
            print("ac:",calculate_acc(test_data_set_y, prediction_y))
            print("f1:",calculate_f1(test_data_set_y, prediction_y))
            with open(save_md_path, "w",encoding="utf-8") as fw:
                fw.write(metrics.head().to_markdown())
            with open(save_json_path, "w", encoding="utf-8") as f:
                f.write(mdtojson(metrics.head().to_markdown()))


