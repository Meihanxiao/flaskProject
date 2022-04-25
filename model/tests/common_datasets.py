from pathlib import Path
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

from common.datasets import read_up_dataset
from common.datasets import read_down_dataset
from common.datasets import read_up_single_stock_dataset
from common.datasets import read_down_single_stock_dataset

def test_for_read_up_datasets(
                              path: str = Path(__file__).parent / "../data/toy_up_model.txt",
                              classification_threshold: list = [0,0.05],
                              type: str="cla"
                              )-> list:

    line_num = 0
    with open(path, "r", encoding="utf-8") as fi:
        readlines = fi.readlines()
        for line in readlines:
            line_num += 1
    if type == "cla":
        data_set_x, data_set_cla_y = read_up_dataset(path,classification_threshold,type)
        assert len(data_set_x) == line_num-1, "the dimension of the data_set_x is wrong"
        assert len(data_set_cla_y) == line_num-1, "the dimension of the data_set_cla_y is wrong"
        print(data_set_x[0:2])
        print(data_set_cla_y[0:2])
    else:
        data_set_x, data_set_reg_y = read_up_dataset(path,classification_threshold,type)
        assert len(data_set_x) == line_num-1, "the dimension of the data_set_x is wrong"
        assert len(data_set_reg_y) == line_num-1, "the dimension of the data_set_reg_y is wrong"
        print(data_set_x[0:2])
        print(data_set_reg_y[0:2])
    
def test_for_read_down_datasets(
                              path: str = Path(__file__).parent / "../data/toy_down_model.txt",
                              classification_threshold: list = [0,0.05],
                              type: str="cla"
                              )-> list:
    
    line_num = 0
    with open(path, "r", encoding="utf-8") as fi:
        readlines = fi.readlines()
        for line in readlines:
            line_num += 1
    if type == "cla":
        data_set_x, data_set_cla_y = read_down_dataset(path,classification_threshold,type)
        assert len(data_set_x) == line_num-1, "the dimension of the data_set_x is wrong"
        assert len(data_set_cla_y) == line_num-1, "the dimension of the data_set_cla_y is wrong"
        print(data_set_x[0:2])
        print(data_set_cla_y[0:2])
    else:
        data_set_x, data_set_reg_y = read_down_dataset(path,classification_threshold,type)
        assert len(data_set_x) == line_num-1, "the dimension of the data_set_x is wrong"
        assert len(data_set_reg_y) == line_num-1, "the dimension of the data_set_reg_y is wrong"
        print(data_set_x[0:2])
        print(data_set_reg_y[0:2])    

def test_for_read_up_single_datasets(
                              path: str = Path(__file__).parent / "../data/toy_up_single_sz.002415.txt",
                              classification_threshold: list = [0,0.05],
                              type: str="cla"
                              )-> list:
    
    line_num = 0
    with open(path, "r", encoding="utf-8") as fi:
        readlines = fi.readlines()
        for line in readlines:
            line_num += 1
    if type == "cla":
        data_set_x, data_set_cla_y = read_up_single_stock_dataset(path,classification_threshold,type)
        assert len(data_set_x) == line_num-1, "the dimension of the data_set_x is wrong"
        assert len(data_set_cla_y) == line_num-1, "the dimension of the data_set_cla_y is wrong"
        print(data_set_x[0:2])
        print(data_set_cla_y[0:2])
    else:
        data_set_x, data_set_reg_y = read_up_single_stock_dataset(path,classification_threshold,type)
        assert len(data_set_x) == line_num-1, "the dimension of the data_set_x is wrong"
        assert len(data_set_reg_y) == line_num-1, "the dimension of the data_set_reg_y is wrong"
        print(data_set_x[0:2])
        print(data_set_reg_y[0:2])   

def test_for_read_down_single_datasets(
                              path: str = Path(__file__).parent / "../data/toy_down_single_sz.002415.txt",
                              classification_threshold: list = [0,0.05],
                              type: str="cla"
                              )-> list:
    
    line_num = 0
    with open(path, "r", encoding="utf-8") as fi:
        readlines = fi.readlines()
        for line in readlines:
            line_num += 1
    if type == "cla":
        data_set_x, data_set_cla_y = read_down_single_stock_dataset(path,classification_threshold,type)
        assert len(data_set_x) == line_num-1, "the dimension of the data_set_x is wrong"
        assert len(data_set_cla_y) == line_num-1, "the dimension of the data_set_cla_y is wrong"
        print(data_set_x[0:2])
        print(data_set_cla_y[0:2])
    else:
        data_set_x, data_set_reg_y = read_down_single_stock_dataset(path,classification_threshold,type)
        assert len(data_set_x) == line_num-1, "the dimension of the data_set_x is wrong"
        assert len(data_set_reg_y) == line_num-1, "the dimension of the data_set_reg_y is wrong"
        print(data_set_x[0:2])
        print(data_set_reg_y[0:2])    

if __name__ == "__main__":
    test_for_read_up_datasets(Path(__file__).parent / "data/toy_down_model.txt",[0, 0.01, 0.02, 0.03, 0.04, 0.05],"cla")
    #test_for_read_down_datasets(Path(__file__).parent / "data/toy_down_model.txt",[0, 0.01, 0.02, 0.03, 0.04, 0.05],"reg")
    #test_for_read_up_single_datasets(Path(__file__).parent / "data/toy_up_single_sz.002415_20_8_3.txt",[0, 0.01, 0.02, 0.03, 0.04, 0.05],"cla")
    #test_for_read_down_single_datasets(Path(__file__).parent / "data/toy_down_single_sz.002415_10_3_0.txt",[0, 0.01, 0.02, 0.03, 0.04, 0.05],"reg")
