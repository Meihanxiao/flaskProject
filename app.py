from flask import Flask, render_template, request, flash
from flask_apscheduler import APScheduler

from routes.detail import detail
from routes.login_register import login_register
from routes.go import go
from routes.add import add
from routes.delete import delete
import pymongo
from services.APScheduler_job import JobList

app = Flask(__name__)
app.config["SECRET_KEY"] = 'TPmi4aLWRbyVq8zu9v82dWYW1'

app.config.from_object(JobList())
# app.config.from_object(RunModel())
scheduler = APScheduler()  # 实例化APScheduler
scheduler.init_app(app)  # 把任务列表载入实例flask
scheduler.start()  # 启动任务计划

app.register_blueprint(login_register, url_prefix='')
app.register_blueprint(go, url_prefix='')
app.register_blueprint(add, url_prefix='')
app.register_blueprint(delete, url_prefix='')
app.register_blueprint(detail, url_prefix='')
client = pymongo.MongoClient(host="localhost", port=27017)
db = client.stock
user = db.user
stock = db.stock_all


# 初始加载页面
@app.route('/', methods=['GET', 'POST'])
def start():
    return render_template('stock/login.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
