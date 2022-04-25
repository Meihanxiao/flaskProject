import baostock as bs
import pandas as pd

# 登陆系统 #
from app import app

lg = bs.login()
# 显示登陆返回信息
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)

# 获取证券信息 #
rs = bs.query_stock_industry()
print('query_all_stock respond error_code:'+rs.error_code)
print('query_all_stock respond  error_msg:'+rs.error_msg)

# 打印结果集 #
data_list = []
code_list = []
temp_list = []
temp1_list = []
all_list = []
while (rs.error_code == '0') & rs.next():
    # 获取一条记录，将记录合并在一起
    data_list.append(rs.get_row_data())
for code in data_list:
    code_list.append((code[1]))
for code in code_list:
    # print(1)
    # print(code)
    rs1 = bs.query_stock_basic(code=code)
    rs2 = bs.query_stock_industry(code=code)
    # print('query_stock_basic respond error_code:' + rs.error_code)
    # print('query_stock_basic respond  error_msg:' + rs.error_msg)
    # print(2)
    while (rs1.error_code == '0') & rs1.next():
        temp_list.append(rs1.get_row_data())
        print(temp_list[0][0])
    # print(3)
    while (rs2.error_code == '0') & rs2.next():
        temp1_list.append(rs2.get_row_data())
        # print(temp1_list[0][3])
    all_list.append(temp_list[0][0]+temp_list[0][1]+temp_list[0][2]+temp1_list[0][3])
    # print(4)
    temp_list = []
    temp1_list = []
result = pd.DataFrame(temp1_list, columns=list("ABCD "))
print(result)


# 结果集输出到csv文件 #
result.to_csv("D:\\all_stock.csv", encoding="gbk", index=False)

# 登出系统 #
bs.logout()

if __name__ == '__main__':
    app.run()
