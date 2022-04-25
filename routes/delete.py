from flask import Flask, render_template, request, flash, Blueprint, session, redirect
import pymongo

delete = Blueprint('delete',  __name__)

client = pymongo.MongoClient(host="localhost", port=27017)
db = client.stock
user = db.user
stock_all = db.stock_all


# 删除自选股
@delete.route('/del_self', methods=['GET'])
def del_self():
    stock_id = request.args.get('id')
    username = session.get('username')
    # print(username)
    result = user.find_one({"account": username})
    result['self_choose_stock'].remove(stock_id)
    result['count_self_choose'] = result['count_self_choose']-1
    user.update({'account': username}, result)
    stock = stock_all.find_one({"stock_id": stock_id})
    if_choose = stock['if_choose'] - 1
    stock_all.update_one({'stock_id': stock_id}, {'$set': {'if_choose': if_choose}})
    return redirect('/goSelfChoose')


# 删除长线股
@delete.route('/del_long', methods=['GET'])
def del_long():
    stock_id = request.args.get('id')
    username = session.get('username')
    # print(username)
    result = user.find_one({"account": username})
    result['long_line_stock'].remove(stock_id)
    result['count_long_line'] = result['count_long_line'] - 1
    user.update({'account': username}, result)
    stock = stock_all.find_one({"stock_id": stock_id})
    if_choose = stock['if_choose'] - 1
    stock_all.update_one({'stock_id': stock_id}, {'$set': {'if_choose': if_choose}})
    return redirect('/goLongLine')
