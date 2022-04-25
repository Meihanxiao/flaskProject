import datetime

from flask import Flask, render_template, request, flash, Blueprint, session, make_response, Response
import pymongo


login_register = Blueprint('login_register', __name__)


client = pymongo.MongoClient(host="localhost", port=27017)
db = client.stock
user = db.user
stock = db.stock_all


# 登录
@login_register.route('/login', methods=['GET', 'POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    count = user.find({'account': username, 'password': password}).count()
    if count == 1:
        result = user.find_one({"account": username}, {'self_choose_stock': 1})
        self_choose_stocks = stock.find({"stock_id": {'$in': result['self_choose_stock']}})
        session['username'] = username
        # for self_choose_stock in self_choose_stocks:
        #     print(self_choose_stock)
        return render_template('stock/self_choose.html', self_choose_stocks=self_choose_stocks, username=username)
    else:
        Message = '账号或者密码错误'
        flash(Message)
        return render_template('stock/login.html')


# 注册
@login_register.route('/register', methods=['GET', 'POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    repassword = request.form.get('repassword')
    print(username)
    count = user.find({'account': username}).count()
    if repassword != password:
        Message = '两次输入不相同'
        flash(Message, 'fail')
        return render_template('stock/register.html')
    if count == 1:
        Message1 = '已有此账号'
        flash(Message1, 'fail')
        return render_template('stock/register.html')
    else:
        new_user = {
            'account': username,
            'password': password
        }
        user.insert_one(new_user)
        Message = '注册成功'
        flash(Message, 'success')
        return render_template('stock/register.html')


# 退出登录
@login_register.route('/login_out')
def login_out():
    session.clear()
    return render_template('stock/login.html')
