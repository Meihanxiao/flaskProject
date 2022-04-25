from flask import Flask, render_template, request, flash, Blueprint, session, redirect
import pymongo

add = Blueprint('add', __name__)

client = pymongo.MongoClient(host="localhost", port=27017)
db = client.stock
user = db.user
stock_all = db.stock_all
stock_basic = db.stock_basic
stock_daily = db.stock_daily


# 添加自选股
@add.route('/add_self', methods=['GET', 'POST'])
def add_self_choose_stock():
    stock_id = request.args.get('id')  # 添加的自选股id
    username = session.get('username')

    new_self_stock = stock_all.find_one({"stock_id": stock_id})
    print(new_self_stock)
    if new_self_stock is not None:
        results = user.find_one({"account": username})
        for result in results['self_choose_stock']:
            if stock_id == result:
                Message = '已加入该股票'
                # flash(Message, 'fail')
                return redirect('/goAddSelfChoose')
        new_self_stock_list = results['self_choose_stock']
        new_self_stock_list.append(stock_id)
        results['self_choose_stock'] = new_self_stock_list
        results['count_self_choose'] = results['count_self_choose']+1
        update_result = user.update_one({'account': username}, {'$set': results})
        if_choose = new_self_stock['if_choose']+1
        stock_all.update_one({'stock_id': stock_id}, {'$set': {'if_choose': if_choose}})
        Message = '添加成功'
        return redirect('/goAddSelfChoose')
    else:
        Message = '股票信息输入有误'
        # flash(Message, 'fail')
        return redirect('/goAddSelfChoose')


# 添加长线股
@add.route('/add_long', methods=['GET', 'POST'])
def add_long_ling_stock():
    stock_id = request.form.get('stock_id')
    # stock_name = request.form.get('stock_name')
    # stock_industry = request.form.get('stock_industry')
    new_long_stock = stock_all.find_one({"stock_id": stock_id})
    username = session.get('username')
    if new_long_stock is not None:
        # username = session.get('username')
        results = user.find_one({"account": username})
        for result in results['long_line_stock']:
            if stock_id == result:
                Message = '已加入该股票'
                # flash(Message, 'fail')
                return redirect('/goAddLongLine')
        new_long_stock_list = results['long_line_stock']
        new_long_stock_list.append(stock_id)
        results['long_line_stock'] = new_long_stock_list
        results['count_long_line'] = results['count_long_line'] + 1
        update_result = user.update_one({'account': username}, {'$set': results})
        if_choose = new_long_stock['if_choose'] + 1
        stock_all.update_one({'stock_id': stock_id}, {'$set': {'if_choose': if_choose}})
        Message = '添加成功'
        # flash(Message, "success")
        return redirect('/goAddLongLine')
    else:
        Message = '股票信息输入有误'
        # flash(Message, 'fail')
        return redirect('/goAddLongLine')
