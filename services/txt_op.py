from flask import Flask
from flask_apscheduler import APScheduler


# 文件操作
def lines(file_list):
    for flie in file_list:
        path = "D:/study/code/pycharmcode/flaskProject/model/data/up/"+flie
        with open(file=path, mode="r") as f1:
            lines = f1.readlines()
            last_line = lines[-1]
            index0 = last_line.find(',')
            index1 = last_line.find(',', index0+1)
            last_line = last_line[0:index0] + last_line[index1:]
        with open(file="D:/study/code/pycharmcode/flaskProject/model/data/up/test.txt", mode="a") as f2:
            f2.write(last_line)

