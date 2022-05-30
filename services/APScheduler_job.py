import pymongo


client = pymongo.MongoClient(host="localhost", port=27017)
db = client.stock
user = db.user
stock_all = db.stock_all  # 查询股票预测信息
stock_basic = db.stock_basic  # 查询股票基本信息
stock_daily = db.stock_daily  # 每日真实数据，包括换手率


# 任务配置类
class JobList(object):
    JOBS = [
        {
            'id': 'renew_basic_db',  # 更新数据库（基础信息）
            'func': 'services:APSrenew_basic_db.renew_basic_db',  # 任务执行程序
            'args': None,  # 执行程序参数
            'trigger': 'cron',  # 任务执行类型，定时器
            'day_of_week': "0-4",
            'hour': "0-2",
            'minute': 0
        },
        {
            'id': 'renew_daily_db',  # 更新数据库（数据信息日线）比较慢
            'func': 'services:APSrenew_daily_db.renew_daily_db',  # 任务执行程序
            'args': None,  # 执行程序参数
            'trigger': "interval",
            'start_date': '17:00:00',
            'end_date': '23:00:00',
            'minutes': 2,
        },
        {
            'id': 'mark_outmarket',  # 更新数据库（退市信息）
            'func': 'services:APSmark_outmarket.mark_outmarket',  # 任务执行程序
            'args': None,  # 执行程序参数
            'trigger': 'cron',  # 任务执行类型，定时器
            'day_of_week': "0-4",
            'hour': "0-2",
            'minute': 5
        },
        {
            'id': 'renew_db',  # 更新数据库任务
            'func': 'services:APSrenew_db.renew_db',  # 任务执行程序
            'args': None,  # 执行程序参数
            'trigger': 'cron',  # 任务执行类型，定时器
            'day_of_week': "0-4",
            'hour': "0-2",
            'minute': 1
        },
        {
            'id': 'run_lstm',
            'func': 'services:APSlstm.run_lstm',
            'args': None,
            'trigger': "interval",
            'start_date': '17:01:00',
            'end_date': '23:01:00',
            'minutes': 2,
        }
        # ,
        # {
        #     'id': 'run_model',  # 运行模型任务
        #     'func': 'services:APSrun_model.run_model',  # 任务执行程序
        #     'args': None,  # 执行程序参数
        #     'trigger': "interval",
        #     'start_date': '17:01:00',
        #     'end_date': '23:01:00',
        #     'minutes': 2,
        # }
    ]


SCHEDULER_TIMEZONE = 'Asia/Shanghai'
SCHEDULER_API_ENABLED = True

