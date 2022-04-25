from pathlib import Path
import sys
import os
import numpy as np
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

from common.datasets import read_up_dataset
from common.sample_method import sample_method

def test_for_sample_method(data_set_x:np.ndarray=np.asarray([[0, 1, 2],[1,1,1],[2, -1, 0], [1, 3, 2]]),
                           data_set_y:np.ndarray=np.asarray([1, 1, 3, 2]),
                           sample_times:int = 5, # 每个类别的采样数量
                           put_back: bool = 1, # 1 表示有放回的采样；0 表示没有放回的采样
                           ):

    data_set_x_ans, data_set_y_ans = sample_method(data_set_x, data_set_y, sample_times, put_back)
    print(data_set_x_ans,data_set_y_ans)

if __name__ == "__main__":
    data_set_x,data_set_y=read_up_dataset(Path(__file__).parent.parent / "data/train_up_model_20_8_3.txt",[0, 0.01, 0.02, 0.03, 0.04, 0.05],"cla")
    test_for_sample_method(data_set_x,data_set_y,30,1)
