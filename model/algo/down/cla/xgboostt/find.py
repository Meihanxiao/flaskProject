from pathlib import Path
import sys
import os
sys.path.append(os.getcwd())

from algo.up.cla.xgboostt.train_up import train_up
from algo.up.cla.xgboostt.eval_up import test_eval

def find():
    for i in range(1,10,1):
        train_up(n=i)
        print ("n=",i)
        test_eval()


if __name__ == "__main__":
    find()
        
