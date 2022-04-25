from pathlib import Path
import sys
import os
sys.path.append(os.getcwd())

from algo.up.cla.gb.train_up import train_up
from algo.up.cla.gb.eval_up import test_eval

def find():
    for i in range(42,43):
        train_up(n=(i))
        print ("n=",i)
        test_eval()


if __name__ == "__main__":
    find()
 
