import numpy as np

def pre_processing(data_set_x:np.ndarray=np.asarray([[0, 1, 2],[2, -1, 0], [1, 3, 2]])):

    assert isinstance(data_set_x,np.ndarray)

    max = np.max(data_set_x)
    min = np.min(data_set_x)

    if max == min :
        max += pow(10,-10)

    data_set_x=((data_set_x-min)/(max-min))
    
    return data_set_x
    
if __name__ == "__main__":
    pre_processing()