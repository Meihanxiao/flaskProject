import os

from flask import Flask
from flask_apscheduler import APScheduler


# 文件操作
def lines(file_list):
    file_path = "D:\\study\\code\\pycharmcode\\flaskProject\\model\\data\\up\\"
    # file_path = "/usr/local/flaskProject/model/data/up/"
    test_path = "D:\\study\\code\\pycharmcode\\flaskProject\\model\\data\\up\\test.txt"
    # test_path = "/usr/local/flaskProject/model/data/up/test.txt"
    for file in file_list:
        path = file_path + file
        with open(file=path, mode="r") as f1:
            line = f1.readlines()
            last_line = line[-1]
            index0 = last_line.find(',')
            index1 = last_line.find(',', index0+1)
            last_line = last_line[0:index0] + last_line[index1:]
        with open(file=test_path, mode="a") as f2:
            f2.write(last_line)

def lines1(file_list):
    file_path = "D:\\study\\code\\pycharmcode\\flaskProject\\model\\data\\down\\"
    # file_path = "/usr/local/flaskProject/model/data/down/"
    test_path = "D:\\study\\code\\pycharmcode\\flaskProject\\model\\data\\down\\test.txt"
    # test_path = "/usr/local/flaskProject/model/data/down/test.txt"
    for file in file_list:
        path = file_path + file
        with open(file=path, mode="r") as f1:
            line = f1.readlines()
            last_line = line[-1]
            index0 = last_line.find(',')
            index1 = last_line.find(',', index0+1)
            last_line = last_line[0:index0] + last_line[index1:]
        with open(file=test_path, mode="a") as f2:
            f2.write(last_line)

if __name__ == "__main__":
    lines1()
