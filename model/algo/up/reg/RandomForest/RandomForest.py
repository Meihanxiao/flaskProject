import pickle 
import os 
import sys
import numpy as np 
from pathlib import Path
from sklearn.ensemble import RandomForestRegressor
sys.path.append(os.getcwd())
from model.common.datasets import read_up_dataset
#from data_processing import post_processing

def RandomForest_process(
                train_path: str = Path(__file__).parent.parent.parent / "../data/toy_train_up_model_20_8_3.txt", 
                model_save_path: str = Path(__file__).parent / "save_model/toy_up_model.pickle",
                classification_threshold: list = [0,0.05],
                type:str = "reg",
                n:float = 100
                ):
    
    train_data_set_x, train_data_set_y = read_up_dataset(train_path, classification_threshold, type)        
    

    clf = RandomForestRegressor().fit(train_data_set_x, train_data_set_y)

    with open(model_save_path,'wb') as f: 
        pickle.dump(clf,f)
    