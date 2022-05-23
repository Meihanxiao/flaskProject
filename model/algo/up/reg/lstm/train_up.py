from pathlib import Path
import sys
import os
sys.path.append(os.getcwd())

from algo.up.reg.lstm.lstm import lstm

def train_up(n:float =100):
    train_path = Path(__file__).parent.parent.parent / "../../data/up/20_0_0_3_train_up_model.txt"
    print(train_path)
    model_save_path = Path(__file__) / "../save_model/20_0_0_3_train_up_model.ckpt"
    save_model_path = Path(__file__) / "../save_model"
    if not os.path.exists(save_model_path):
        os.makedirs(save_model_path)
    assert os.path.exists(train_path) == True
    
    lstm(train_path, model_save_path, "reg",n=n)


if __name__ == "__main__":
    train_up(n=100)  