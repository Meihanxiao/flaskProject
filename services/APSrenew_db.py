import pymongo
import baostock as bs


client = pymongo.MongoClient(host="localhost", port=27017)
db = client.stock
user = db.user
stock_all = db.stock_all  # 查询股票预测信息
stock_basic = db.stock_basic  # 查询股票基本信息
stock_daily = db.stock_daily  # 每日真实数据，包括换手率


# 定义任务执行程序（每日更新数据库）
def renew_db():
    print("正在执行renew_db的任务-------------------------------------------")
    # 登陆系统
    lg = bs.login()

    # 获取行业分类数据
    rs = bs.query_stock_basic()

    code_list = []  # 数据库

    new_data = db.stock_all.find()  # 数据库中id
    for data in new_data:
        code_list.append(data['stock_id'])

    # print(code_list)

    # 获取行业分类数据
    print('query_stock_industry error_code:' + rs.error_code)
    print('query_stock_industry respond  error_msg:' + rs.error_msg)

    # 打印结果集
    industry_lists = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        industry_lists.append(rs.get_row_data())

    code_list1 = []  # 接口
    for industry_list in industry_lists:
        code_list1.append(industry_list[0])
    # print(code_list1)

    set_1 = set(code_list)
    new_list = [item for item in code_list1 if item not in set_1]
    print(new_list)

    for code in new_list:
        stock1 = bs.query_stock_basic(code).get_row_data()
        # print(stock1)
        stock_id = stock1[0]
        stock_name = stock1[1]
        stock_time_to_market = stock1[2]
        stock2 = bs.query_stock_industry(code).get_row_data()
        if stock2:
            stock_industry = stock2[3]
        else:
            stock_industry = ''
        print("1:")
        print(stock2)
        new_stock = {
            'stock_id': stock_id,
            'stock_name': stock_name,
            'stock_time_to_market': stock_time_to_market,
            'stock_industry': stock_industry,
            'stock_data': []
        }
        stock_all.insert_one(new_stock)
        # print(new_stock)
    # 登出系统
    bs.logout()
    print("更新成功")


if __name__ == "__main__":
    renew_db()
