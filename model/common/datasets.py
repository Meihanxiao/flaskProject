import numpy as np
from pathlib import Path

def read_up_dataset(
                    path: str = Path(__file__).parent / "../data/toy_up_model.txt",
                    classification_threshold: list = [0,0.05],
                    type: str="cla"
                    ) -> list:

    data_set_x = []
    if type == "cla":
        length = len(classification_threshold)
        assert length > 0, "please fill classification_threshold" 
        data_set_cla_y = []
    else:
        data_set_reg_y = []
    with open(path, "r", encoding="utf-8") as fi:
        readlines = fi.readlines()
        line_num = 0
        for line in readlines:
            if line_num == 0:
                line_num += 1
                continue
            line = line.split(',')
            target = float(line[2])
            if type=="cla":
                number = 0
                label = length+1
                while (number < length):
                    number += 1
                    if target < classification_threshold[number - 1]:
                        label = number
                        break 
                assert isinstance(label,int) and label > 0 and label < length + 2,  "label in [1,2,3...]"
                data_set_cla_y.append(label)                
            else:
                data_set_reg_y.append(target)
            data_set_x.append([float(value) for value in line[3:]])
        if type=="cla":
            data_set_cla_y = np.array(data_set_cla_y)
        else :
            data_set_reg_y = np.array(data_set_reg_y)
        data_set_x = np.array(data_set_x)
    if type=="cla":
        assert isinstance(data_set_cla_y,np.ndarray), "data_set_cla_y is not a ndarray"
    else :
        assert isinstance(data_set_reg_y,np.ndarray), "data_set_reg_y is not a ndarray"
    assert isinstance(data_set_x,np.ndarray), "data_set_x is not a ndarray"
    
    if type == "cla":
        return data_set_x, data_set_cla_y
    elif type =="reg":
        return data_set_x, data_set_reg_y


def read_down_dataset(
                    path: str = Path(__file__).parent / "../data/toy_down_model.txt",
                    classification_threshold: list = [0,0.05],
                    type: str="cla"
                    ) -> list:

    data_set_x = []
    if type == "cla":
        length = len(classification_threshold)
        assert length > 0, "please fill classification_threshold" 
        data_set_cla_y = []
    else:
        data_set_reg_y = []
    with open(path, "r", encoding="utf-8") as fi:
        readlines = fi.readlines()
        line_num = 0
        for line in readlines:
            if line_num == 0:
                line_num += 1
                continue
            line = line.split(',')
            target = float(line[2])
            if type=="cla":
                number = 0
                label = length+1
                while (number < length):
                    number += 1
                    if target < classification_threshold[number - 1]:
                        label = number
                        break 
                assert isinstance(label,int) and label > 0 and label < length + 2,  "label in [1,2,3...]"
                data_set_cla_y.append(label)                
            else:
                data_set_reg_y.append(target)
            data_set_x.append([float(value) for value in line[3:]])
        if type=="cla":
            data_set_cla_y = np.array(data_set_cla_y)
        else :
            data_set_reg_y = np.array(data_set_reg_y)
        data_set_x = np.array(data_set_x)
    if type=="cla":
        assert isinstance(data_set_cla_y,np.ndarray), "data_set_cla_y is not a ndarray"
    else :
        assert isinstance(data_set_reg_y,np.ndarray), "data_set_reg_y is not a ndarray"
    assert isinstance(data_set_x,np.ndarray), "data_set_x is not a ndarray"
    
    if type == "cla":
        return data_set_x, data_set_cla_y
    elif type =="reg":
        return data_set_x, data_set_reg_y

def read_up_single_stock_dataset(
                                 path: str = Path(__file__).parent / "../data/toy_up_single_sz.002415.txt",
                                 classification_threshold: list = [0,0.05],
                                 type: str="cla"
                                ) -> list:
    
    data_set_x = []
    if type == "cla":
        length = len(classification_threshold)
        assert length > 0, "please fill classification_threshold" 
        data_set_cla_y = []
    else:
        data_set_reg_y = []
    with open(path, "r", encoding="utf-8") as fi:
        readlines = fi.readlines()
        line_num = 0
        for line in readlines:
            if line_num == 0:
                line_num += 1
                continue
            line = line.split(',')
            target = float(line[3])
            if type=="cla":
                number = 0
                label = length+1
                while (number < length):
                    number += 1
                    if target < classification_threshold[number - 1]:
                        label = number
                        break 
                assert isinstance(label,int) and label > 0 and label < length + 2,  "label in [1,2,3...]"
                data_set_cla_y.append(label)                
            else:
                data_set_reg_y.append(target)
            data_set_x.append([float(value) for value in line[4:]])
        if type=="cla":
            data_set_cla_y = np.array(data_set_cla_y)
        else :
            data_set_reg_y = np.array(data_set_reg_y)
        data_set_x = np.array(data_set_x)
    if type=="cla":
        assert isinstance(data_set_cla_y,np.ndarray), "data_set_cla_y is not a ndarray"
    else :
        assert isinstance(data_set_reg_y,np.ndarray), "data_set_reg_y is not a ndarray"
    assert isinstance(data_set_x,np.ndarray), "data_set_x is not a ndarray"
    
    if type == "cla":
        return data_set_x, data_set_cla_y
    elif type =="reg":
        return data_set_x, data_set_reg_y

def read_down_single_stock_dataset(
                                   path: str = Path(__file__).parent / "../data/toy_down_single_sz.002415.txt",
                                   classification_threshold: list = [0,0.05],
                                   type: str="cla"
                                   ) -> list:
    
    data_set_x = []
    if type == "cla":
        length = len(classification_threshold)
        assert length > 0, "please fill classification_threshold" 
        data_set_cla_y = []
    else:
        data_set_reg_y = []
    with open(path, "r", encoding="utf-8") as fi:
        readlines = fi.readlines()
        line_num = 0
        for line in readlines:
            if line_num == 0:
                line_num += 1
                continue
            line = line.split(',')
            target = float(line[3])
            if type=="cla":
                number = 0
                label = length+1
                while (number < length):
                    number += 1
                    if target < classification_threshold[number - 1]:
                        label = number
                        break 
                assert isinstance(label,int) and label > 0 and label < length + 2,  "label in [1,2,3...]"
                data_set_cla_y.append(label)                
            else:
                data_set_reg_y.append(target)
            data_set_x.append([float(value) for value in line[4:]])
        if type=="cla":
            data_set_cla_y = np.array(data_set_cla_y)
        else :
            data_set_reg_y = np.array(data_set_reg_y)
        data_set_x = np.array(data_set_x)
    if type=="cla":
        assert isinstance(data_set_cla_y,np.ndarray), "data_set_cla_y is not a ndarray"
    else :
        assert isinstance(data_set_reg_y,np.ndarray), "data_set_reg_y is not a ndarray"
    assert isinstance(data_set_x,np.ndarray), "data_set_x is not a ndarray"
    
    if type == "cla":
        return data_set_x, data_set_cla_y
    elif type =="reg":
        return data_set_x, data_set_reg_y

