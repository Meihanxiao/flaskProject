import datetime
from dateutil.relativedelta import relativedelta
from flask import Flask, render_template, request, flash, Blueprint, session
import baostock as bs
import pandas as pd
import time
from dateutil import parser
import pymongo

go = Blueprint('go', __name__)

client = pymongo.MongoClient(host="localhost", port=27017)
db = client.stock
user = db.user
stock_all = db.stock_all
stock_basic = db.stock_basic
stock_daily = db.stock_daily


# 转到登录页面
@go.route('/goLogin', methods=['GET'])
def go_login():
    return render_template('stock/login.html')


# 转到注册页面
@go.route('/goRegister', methods=['GET'])
def go_register():
    return render_template('stock/register.html')


# 跳转到自选股界面
@go.route('/goSelfChoose')
def go_selfChoose():
    username = session.get('username')
    # print(username)
    result = user.find_one({"account": username}, {'self_choose_stock': 1})
    print(result['self_choose_stock'])
    self_choose_stocks = stock_all.find({"stock_id": {'$in': result['self_choose_stock']}})
    return render_template('stock/self_choose.html', self_choose_stocks=self_choose_stocks, username=username)


# 跳转到长线股界面
@go.route('/goLongLine')
def go_longline():
    username = session.get('username')
    # print(username)
    result = user.find_one({"account": username}, {'long_line_stock': 1})
    long_line_stocks = stock_all.find({"stock_id": {'$in': result['long_line_stock']}})
    return render_template('stock/long_line.html', long_line_stocks=long_line_stocks, username=username)


# 跳转到上市一年股票界面
@go.route('/goOneYear')
def go_oneYear():
    username = session.get('username')
    start_date = (datetime.datetime.now() + relativedelta(years=-1)).strftime("%Y-%m-%dT00:00:00.000Z")
    start_date = parser.parse(start_date)
    end_date = (datetime.datetime.now() + relativedelta(months=-11)).strftime("%Y-%m-%dT00:00:00.000Z")
    end_date = parser.parse(end_date)
    time_condition = {"stock_time_to_market": {'$gt': start_date, '$lt': end_date}}
    name_condition = {"$or": [{"stock_id": {'$regex': '^sh.6'}}, {"stock_id": {'$regex': '^sz.00'}}, {"stock_id": {'$regex': '^sz.30'}}]}
    one_year_stocks = stock_all.find({"$and": [time_condition, name_condition]})
    # one_year_stocks = stock_all.find({"stock_time_to_market": {'$gt': start_date, '$lt': end_date}})
    return render_template('stock/one_year.html', one_year_stocks=one_year_stocks, username=username)


# 跳转到上市三年股票界面
@go.route('/goThreeYear')
def go_threeyear():
    username = session.get('username')
    start_date = (datetime.datetime.now() + relativedelta(years=-3)).strftime("%Y-%m-%dT00:00:00.000Z")
    start_date = parser.parse(start_date)
    end_date = (datetime.datetime.now() + relativedelta(months=-35)).strftime("%Y-%m-%dT00:00:00.000Z")
    end_date = parser.parse(end_date)
    time_condition = {"stock_time_to_market": {'$gt': start_date, '$lt': end_date}}
    name_condition = {"$or": [{"stock_id": {'$regex': '^sh.6'}}, {"stock_id": {'$regex': '^sz.00'}},
                              {"stock_id": {'$regex': '^sz.30'}}]}
    three_year_stocks = stock_all.find({"$and": [time_condition, name_condition]})
    return render_template('stock/three_year.html', three_year_stocks=three_year_stocks, username=username)


# 跳转到最近上市股票界面
@go.route('/goRecent')
def go_Recent():
    username = session.get('username')
    start_date = (datetime.datetime.now() + relativedelta(days=-60)).strftime("%Y-%m-%dT00:00:00.000Z")
    start_date = parser.parse(start_date)
    end_date = (datetime.datetime.now() + relativedelta(days=-59)).strftime("%Y-%m-%dT00:00:00.000Z")
    end_date = parser.parse(end_date)
    time_condition = {"stock_time_to_market": {'$gt': start_date, '$lt': end_date}}
    name_condition = {"$or": [{"stock_id": {'$regex': '^sh.6'}}, {"stock_id": {'$regex': '^sz.00'}}, {"stock_id": {'$regex': '^sz.30'}}]}
    recent_stocks = stock_all.find({"$and": [time_condition, name_condition]})
    return render_template('stock/recent_stock.html', recent_stocks=recent_stocks, username=username)


# 跳转到添加自选股界面
@go.route('/goAddSelfChoose')
def go_add_selfchoose():
    username = session.get('username')
    name_condition = {"$or": [{"stock_id": {'$regex': '^sh.6'}}, {"stock_id": {'$regex': '^sz.00'}},
                              {"stock_id": {'$regex': '^sz.30'}}]}
    add_self_stocks = stock_all.find(name_condition)
    return render_template('stock/add_self_choose.html', username=username, add_self_stocks=add_self_stocks)


# 跳转到添加长线股
@go.route('/goAddLongLine')
def go_add_longline():
    username = session.get('username')
    name_condition = {"$or": [{"stock_id": {'$regex': '^sh.6'}}, {"stock_id": {'$regex': '^sz.00'}},
                              {"stock_id": {'$regex': '^sz.30'}}]}
    add_long_stocks = stock_all.find(name_condition)
    return render_template('stock/add_long_line.html', username=username, add_long_stocks=add_long_stocks)


# 跳转到每日信息界面
@go.route('/goMessage')
def go_message():
    username = session.get('username')
    return render_template('stock/message.html', username=username)


# 跳转到每日信息界面
@go.route('/goHot')
def go_hot():
    username = session.get('username')
    hot_stocks = stock_daily.find().sort('turn', pymongo.DESCENDING).limit(50)
    return render_template('stock/hot.html', username=username, hot_stocks=hot_stocks)


