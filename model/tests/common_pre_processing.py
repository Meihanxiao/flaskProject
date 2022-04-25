from pathlib import Path
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
from common.backtest import read_up_dataset
from common.pre_processing import pre_processing

def test_for_pre_processing(data_set_x:list =[[0, 1],[2, 1]],type = 'up'):

    data_set_x_std = pre_processing(data_set_x,type)
    print(data_set_x_std)
    assert len(data_set_x) == len(data_set_x_std)
    assert len(data_set_x[0]) == len(data_set_x_std[0])

if __name__ == "__main__":
    data_set_x, data_set_reg_y =read_up_dataset(path=Path(__file__).parent / "../data/toy_test_up_model_20_8_3.txt", type = 'reg')
    test_for_pre_processing(data_set_x,'up')