import json
from flask import Flask, render_template, request, flash, Blueprint, session, redirect
import pymongo

detail = Blueprint('detail',  __name__)

client = pymongo.MongoClient(host="localhost", port=27017)
db = client.stock
user = db.user
stock = db.stock_all


# 查看自选股预测上涨详情
@detail.route('/goSelfDetailUp', methods=['GET'])
def go_self_detail_up():
    stock_id = request.args.get('id')
    session['stock_id'] = stock_id
    this_stock = stock.find_one({"stock_id": stock_id})
    stock_name = this_stock['stock_name']
    if this_stock['stock_industry'] is None:
        stock_industry = ""
    else:
        stock_industry = this_stock['stock_industry']
    stock_details = stock.find_one({"stock_id": stock_id})
    for stock_detail in stock_details['stock_data']:
        print(stock_detail['date'])
    return render_template('stock/self_choose_detail_up.html', stock_datas=stock_details['stock_data'], stock_id=stock_id,
                           stock_name=stock_name, stock_industry=stock_industry)


# 查看自选股预测下跌详情
@detail.route('/goSelfDetailDown', methods=['GET'])
def go_self_detail_down():
    stock_id = request.args.get('id')
    username = session.get('username')
    session['stock_id'] = stock_id
    this_stock = stock.find_one({"stock_id": stock_id})
    stock_name = this_stock['stock_name']
    stock_industry = this_stock['stock_industry']
    stock_details = stock.find_one({"stock_id": stock_id})
    for stock_detail in stock_details['stock_data']:
        print(stock_detail)
    return render_template('stock/self_choose_detail_down.html', stock_datas=stock_details['stock_data'], stock_id=stock_id,
                           stock_name=stock_name, stock_industry=stock_industry, username=username)


# 查看长线股预测上涨详情
@detail.route('/goLongDetailUp', methods=['GET'])
def go_long_detail_up():
    stock_id = request.args.get('id')
    username = session.get('username')
    session['stock_id'] = stock_id
    this_stock = stock.find_one({"stock_id": stock_id})
    stock_name = this_stock['stock_name']
    stock_industry = this_stock['stock_industry']
    stock_details = stock.find_one({"stock_id": stock_id})
    # for stock_detail in stock_details['stock_data']:
    #     print(stock_detail.stock_daily_predict_up)
    return render_template('stock/long_line_detail_up.html', stock_datas=stock_details['stock_data'], stock_id=stock_id,
                           stock_name=stock_name, stock_industry=stock_industry, username=username)


# 查看长线股预测下跌详情
@detail.route('/goLongDetailDown', methods=['GET'])
def go_long_detail_down():
    stock_id = request.args.get('id')
    username = session.get('username')
    session['stock_id'] = stock_id
    this_stock = stock.find_one({"stock_id": stock_id})
    stock_name = this_stock['stock_name']
    stock_industry = this_stock['stock_industry']
    stock_details = stock.find_one({"stock_id": stock_id})
    for stock_detail in stock_details['stock_data']:
        print(stock_detail)
    return render_template('stock/long_line_detail_down.html', stock_datas=stock_details['stock_data'], stock_id=stock_id,
                           stock_name=stock_name, stock_industry=stock_industry, username=username)


# 绘制自选上涨图表
@detail.route('/selfUpChart')
def self_up_chart():
    stock_id = session.get('stock_id')
    stock_details = stock.find_one({"stock_id": stock_id})
    session.pop('stock_id')
    print(stock_details)
    day_lists = []
    predict_data_lists = []
    real_data_lists = []
    count = 0
    for stock_detail in stock_details['stock_data']:
        if count < 7:
            predict_data_lists.append(stock_detail['stock_daily_predict_up'])
            real_data_lists.append(stock_detail['stock_daily_real_up'])
            day_lists.append(stock_detail['date'])
            count = count+1
        else:
            break
    return json.dumps({'predict_data_lists': predict_data_lists, 'real_data_lists': real_data_lists, 'day_lists': day_lists}, ensure_ascii=False)


# 绘制自选下跌图表
@detail.route('/selfDownChart')
def self_Down_chart():
    stock_id = session.get('stock_id')
    stock_details = stock.find_one({"stock_id": stock_id})
    session.pop('stock_id')
    print(stock_details)
    day_lists = []
    predict_data_lists = []
    real_data_lists = []
    count = 0
    for stock_detail in stock_details['stock_data']:
        if count < 7:
            predict_data_lists.append(stock_detail['stock_daily_predict_down'])
            real_data_lists.append(stock_detail['stock_daily_real_down'])
            day_lists.append(stock_detail['date'])
            count = count+1
        else:
            break
    return json.dumps({'predict_data_lists': predict_data_lists, 'real_data_lists': real_data_lists, 'day_lists': day_lists}, ensure_ascii=False)


# 绘制长线上涨图表
@detail.route('/longUpChart')
def long_Up_chart():
    stock_id = session.get('stock_id')
    stock_details = stock.find_one({"stock_id": stock_id})
    session.pop('stock_id')
    print(stock_details)
    day_lists = []
    predict_data_lists = []
    real_data_lists = []
    count = 0
    for stock_detail in stock_details['stock_data']:
        if count < 7:
            predict_data_lists.append(stock_detail['stock_daily_predict_up'])
            real_data_lists.append(stock_detail['stock_daily_real_up'])
            day_lists.append(stock_detail['date'])
            count = count+1
        else:
            break
    return json.dumps({'predict_data_lists': predict_data_lists, 'real_data_lists': real_data_lists, 'day_lists': day_lists}, ensure_ascii=False)


# 绘制长线下跌图表
@detail.route('/longDownChart')
def long_Down_chart():
    stock_id = session.get('stock_id')
    stock_details = stock.find_one({"stock_id": stock_id})
    session.pop('stock_id')
    print(stock_details)
    day_lists = []
    predict_data_lists = []
    real_data_lists = []
    count = 0
    for stock_detail in stock_details['stock_data']:
        if count < 7:
            predict_data_lists.append(stock_detail['stock_daily_predict_down'])
            real_data_lists.append(stock_detail['stock_daily_real_down'])
            day_lists.append(stock_detail['date'])
            count = count+1
        else:
            break
    return json.dumps({'predict_data_lists': predict_data_lists, 'real_data_lists': real_data_lists, 'day_lists': day_lists}, ensure_ascii=False)
