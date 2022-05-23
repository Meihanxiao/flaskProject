import pickle 
import os 
import sys
from pathlib import Path 
from sklearn.svm import SVR
sys.path.append(os.getcwd())
from common.datasets import read_up_dataset
#from data_processing import post_processing

def svm_process(
                train_path: str = Path(__file__).parent.parent.parent / "../data/toy_train_up_model_20_8_3.txt", 
                model_save_path: str = Path(__file__).parent / "save_model/toy_up_model.pickle",
                type:str = "reg"
                ):
    
    train_data_set_x, train_data_set_y = read_up_dataset(path= train_path, type= type)

    # do some post processing here
    #train_data_set_x = post_processing(train_data_set_x)

    clf = SVR(kernel="rbf")
    clf = clf.fit(train_data_set_x, train_data_set_y)

    with open(model_save_path,'wb') as f: 
        pickle.dump(clf,f)