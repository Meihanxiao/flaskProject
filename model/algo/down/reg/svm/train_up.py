from pathlib import Path
import sys
import os
sys.path.append(os.getcwd())

from algo.up.reg.svm.svm import svm_process

def train_up():
    train_path = Path(__file__).parent.parent.parent / "../data/toy_train_up_model_20_8_3.txt"
    model_save_path = Path(__file__) / "../save_model/toy_up_model.pickle"
    save_model_path = Path(__file__) / "../save_model"
    if not os.path.exists(save_model_path):
        os.makedirs(save_model_path)
    assert os.path.exists(train_path) == True
    svm_process(train_path, model_save_path,"reg")


if __name__ == "__main__":
    train_up()
