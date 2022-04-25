import pickle 
import os 
import sys
import numpy as np 
from pathlib import Path 
from sklearn.ensemble import RandomForestClassifier
sys.path.append(os.getcwd())
from common.datasets import read_up_dataset
#from data_processing import post_processing

def RandomForest_process(
                train_path: str = Path(__file__).parent.parent.parent / "../data/toy_train_up_model_20_8_3.txt", 
                model_save_path: str = Path(__file__).parent / "save_model/toy_up_model.pickle",
                classification_threshold: list = [0,0.05],
                type:str = "cla",
                n:float = 100
                ):
    
    train_data_set_x, train_data_set_y = read_up_dataset(train_path, classification_threshold, type)
    
    debug = 0
    if debug == 0:
        train_x, train_y = [], []
        label_num = []
        for i in range (len(classification_threshold)+2):
            label_num .append(325)
        print(label_num)
     #   two = 325
      #  one = 325   # lable = 1 的数量
        for i in range(len(train_data_set_y)):
            if label_num[train_data_set_y[i]] >0:
                label_num[train_data_set_y[i]]-=1
                train_x.append(train_data_set_x[i])
                train_y.append(train_data_set_y[i])
            
        train_data_set_x = np.array(train_x)
        train_data_set_y = np.array(train_y)


    if debug==1:
        print(train_data_set_y)
        stat = {}
        for item in train_data_set_y:
            if item not in stat:
                stat[item] = 1
            else:
                stat[item] += 1
        print(stat)
        

    # do some post processing here
    #train_data_set_x = post_processing(train_data_set_x)

    

    clf = RandomForestClassifier(n_estimators=85,random_state=90,max_depth=n).fit(train_data_set_x, train_data_set_y)

    with open(model_save_path,'wb') as f: 
        pickle.dump(clf,f)
    