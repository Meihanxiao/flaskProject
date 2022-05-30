import csv
import datetime

import tushare as ts
import pandas as pd
import numpy as np
import tensorflow as tf
import sklearn
from dateutil.relativedelta import relativedelta
from matplotlib import pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow_core.python.keras import Sequential
from tensorflow_core.python.keras.layers import LSTM, Dropout, Dense


def download_data(code):
    ts.set_token('bd74770b73ea294d073763c1f8a8157b8de68fc76d4800c1f23d3ee0')
    # 我获取的是前复权的数据，如果不需要复权可以调用ts.daily() 600519.SH
    start_data = (datetime.datetime.now() + relativedelta(years=-1)).strftime("%Y%m%d")
    train_data = ts.pro_bar(ts_code=code, adj='qfq',  end_date=start_data)
    train_data.to_csv('data/'+code+'_train_data.csv')
    end_time = datetime.datetime.now().strftime("%Y%m%d")
    # print(end_time)
    test_data = ts.pro_bar(ts_code=code, adj='qfq', start_date=start_data, end_date=end_time)
    test_data.to_csv('data/'+code+'_test_data.csv')


def prepare_data(code):
    train_data = pd.read_csv('data/'+code+'_train_data.csv', index_col=['trade_date'])
    test_data = pd.read_csv('data/'+code+'_test_data.csv', index_col=['trade_date'])
    # 因为tushare获取的日期是从最新开始获取，所以在进行预测前要reverse
    train_data, test_data = train_data[::-1], test_data[::-1]
    # 原始数据的维度只需要作为输入【开盘价，最高价，最低价，涨跌幅，成交量】
    # 因为我只想要得到后一天收盘价的预测结果，所以预测的指导向量是【收盘价】
    train_data = train_data[[ 'open', 'high', 'low' , 'pct_chg', 'vol', 'close']]
    print(train_data)
    test_data = test_data[[ 'open', 'high', 'low' , 'pct_chg', 'vol', 'close']]
    print(test_data)
    train_data.index.name = 'date'
    test_data.index.name = 'date'


def clean_data(code):
    df = pd.read_csv('data/'+code+'_train_data.csv', index_col=0)
    res = df[df["pct_chg"].map(pd.isna) == False]
    res.to_csv('data/'+code+'_train_data.csv', sep=',')


def train_data(time_step, sx, sy, code):
    train_data = pd.read_csv('data/'+code+'_train_data.csv')
    train_data = train_data[::-1]
    # 数据归一化
    # sc = MinMaxScaler(feature_range=(0, 1))
    # X_train = train_data[['open', 'high', 'low', 'vol', 'close']]
    # Y_train = train_data[['pct_chg']]
    X_train = train_data[['open', 'high', 'low', 'pct_chg', 'vol']]
    Y_train = train_data[['close']]

    X_train = sx.fit_transform(X_train)
    Y_train = sy.fit_transform(Y_train)

    x_train, y_train = [], []
    for i in range(time_step, train_data.shape[0]):
        x_train.append(X_train[i - time_step:i, :])
        y_train.append(Y_train[i])
    x_train, y_train = np.array(x_train), np.array(y_train)
    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 5))
    # print(x_train, y_train, sx, sy)
    return x_train, y_train, sx, sy


def train_data1(time_step, sx, sy, code):
    train_data = pd.read_csv('data/'+code+'_train_data.csv')
    train_data = train_data[::-1]
    X_train = train_data[['high', 'low', 'pct_chg', 'vol', 'close']]
    Y_train = train_data[['open']]

    X_train = sx.fit_transform(X_train)
    Y_train = sy.fit_transform(Y_train)

    x_train, y_train = [], []
    for i in range(time_step, train_data.shape[0]):
        x_train.append(X_train[i - time_step:i, :])
        y_train.append(Y_train[i])
    x_train, y_train = np.array(x_train), np.array(y_train)
    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 5))
    # print(x_train, y_train, sx, sy)
    return x_train, y_train, sx, sy


def test_data(time_step, sxx, syy, code):
    train_data = pd.read_csv('data/'+code+'_train_data.csv')
    test_data = pd.read_csv('data/'+code+'_test_data.csv')
    train_data, test_data = train_data[::-1], test_data[::-1]
    all_data = pd.concat((train_data, test_data), axis=0)
    # all_data = all_data[::-1]
    # print(all_data)

    # X_all = all_data[['open', 'high', 'low', 'vol', 'close']]
    # Y_all = all_data[['pct_chg']]
    X_all = all_data[['open', 'high', 'low', 'pct_chg', 'vol']]
    Y_all = all_data[['close']]
    x_test, y_test = [], []
    #     print(len(all_data), len(test_data), time_step)
    X_all = X_all[len(all_data) - len(test_data) - time_step:]
    print(X_all)
    Y_all = Y_all[len(all_data) - len(test_data) - time_step:]
    print(Y_all)
    X_all = sxx.fit_transform(X_all)
    Y_all = syy.fit_transform(Y_all)
    print(X_all)
    for i in range(time_step, test_data.shape[0]):
        # print(i - time_step, i)
        x_test.append(X_all[i:i + time_step, :])
        y_test.append(Y_all[i + time_step])
    x_test, y_test = np.array(x_test), np.array(y_test)
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 5))
    return x_test, y_test, sxx, syy


def test_data1(time_step, sxx, syy, code):
    train_data = pd.read_csv('data/'+code+'_train_data.csv')
    test_data = pd.read_csv('data/'+code+'_test_data.csv')
    train_data, test_data = train_data[::-1], test_data[::-1]
    all_data = pd.concat((train_data, test_data), axis=0)
    # all_data = all_data[::-1]
    # print(all_data)

    # X_all = all_data[['open', 'high', 'low', 'vol', 'close']]
    # Y_all = all_data[['pct_chg']]
    X_all = all_data[['high', 'low', 'pct_chg', 'vol', 'close']]
    Y_all = all_data[['open']]
    x_test, y_test = [], []
    #     print(len(all_data), len(test_data), time_step)
    X_all = X_all[len(all_data) - len(test_data) - time_step:]
    print(X_all)
    Y_all = Y_all[len(all_data) - len(test_data) - time_step:]
    print(Y_all)
    X_all = sxx.fit_transform(X_all)
    Y_all = syy.fit_transform(Y_all)
    print(X_all)
    for i in range(time_step, test_data.shape[0]):
        # print(i - time_step, i)
        x_test.append(X_all[i-1:i + time_step - 1, :])
        y_test.append(Y_all[i + time_step])
    x_test, y_test = np.array(x_test), np.array(y_test)
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 5))
    return x_test, y_test, sxx, syy


def stock_predict(x_train, y_train, x_test, y_test,  _epochs, _steps_per_epoch):
    model = Sequential()
    model.add(LSTM(units=50, activation='relu',
                   input_shape=(x_train.shape[1], x_train.shape[2]),
                   return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50, activation='relu', return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(units=32))
    model.add(Dropout(0.2))
    model.add(Dense(y_train.shape[1], activation='linear'))
    model.compile(loss='mse', optimizer='adam', metrics=['acc'])

    history = model.fit(x_train, y_train, epochs=_epochs, steps_per_epoch=_steps_per_epoch)
    # plt.plot(history.history['loss'], label='Training Loss')
    # plt.plot(history.history['val_loss'], label='Validation Loss')
    # plt.title('loss')
    # plt.legend()
    # plt.show()
    return model


def test(code):
    test_data = pd.read_csv('data/' + code + '_test_data.csv')
    print(test_data.shape[0])


if __name__ == "__main__":
    # clean_data('600006.SH')
    download_data('600000.SH')
    prepare_data('600000.SH')
    # test('600000.SH')

