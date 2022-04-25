
import random
import numpy as np
from collections import Counter


def sample_method(
                  data_set_x:np.ndarray=np.asarray([[0, 1, 2],[1,1,1],[2, -1, 0], [1, 3, 2]]),
                  data_set_y:np.ndarray=np.asarray([1, 1, 3, 2]),
                  sample_times:int = 5, # 每个类别的采样数量
                  put_back: bool = 1, # 1 表示有放回的采样；0 表示没有放回的采样
                  ):
    
    max_label = np.max(data_set_y)
    length = len(data_set_x)
    data_set_x_mid = []
    data_set_y_mid = []
    data_set_x_sam = []
    data_set_y_sam = []
    label_num = np.zeros(max_label+1)
    label_pos = np.zeros(max_label+1)
    label_num[1] = Counter(data_set_y)[1]
    min_num = label_num[1]
    
    for i in range(2,max_label+1):
        label_num[i] = Counter(data_set_y)[i]
        if label_num[i] < min_num :
            min_num = label_num[i]

    for i in range(1, max_label+1):
        label_pos[i] = label_pos[i-1] + label_num[i]

    for i in range(1,max_label+1):
        for j in range(length):
            if data_set_y[j] == i:
                data_set_x_mid.append(data_set_x[j])
                data_set_y_mid.append(data_set_y[j])
    if put_back :
        for i in range(1, max_label+1):
            sum = 0
            while sum < sample_times:
                ra = random.randint(label_pos[i-1],label_pos[i]-1)
                data_set_x_sam.append(data_set_x_mid[ra])
                data_set_y_sam.append(i)
                sum+=1
    else :
        assert min_num >= sample_times ,"Data is missing. Please add data"   
        for i in range(1, max_label+1):
            sum = 0
            rang=[]
            for j in range(int(label_pos[i-1]),int(label_pos[i])):
                rang.append(j)
            while sum < sample_times:
                ra = random.choice(rang)
                data_set_x_sam.append(data_set_x_mid[ra])
                data_set_y_sam.append(i)
                rang.remove(ra)
                sum+=1
    data_set_x_ans=[]
    data_set_y_ans=[]
    rang = []
    for i in range(sample_times*max_label):
        rang.append(i)

    for i in range(sample_times*max_label):
        ra = random.choice(rang)
        data_set_x_ans.append(data_set_x_sam[ra])
        data_set_y_ans.append(data_set_y_sam[ra])
        rang.remove(ra)

    data_set_x_ans = np.array(data_set_x_ans)
    data_set_y_ans = np.array(data_set_y_ans)

    assert len(data_set_x_ans) == sample_times*max_label , "the number of the data_set_y_ans is wrong" 
    assert len(data_set_y_ans) == sample_times*max_label , "the number of the data_set_y_ans is wrong"
    label_num[1] = Counter(data_set_y_ans)[1]
    assert label_num[1] == sample_times 

    return data_set_x_ans,data_set_y_ans
          
if __name__ == "__main__":
    sample_method()

