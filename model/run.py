from matplotlib import pyplot as plt, dates
from sklearn.preprocessing import MinMaxScaler

from model.main import train_data, test_data, stock_predict, train_data1, test_data1, download_data, prepare_data, clean_data


def run_model_open(code):
    sx = MinMaxScaler(feature_range=(0, 1))
    sy = MinMaxScaler(feature_range=(0, 1))
    sxx = MinMaxScaler(feature_range=(0, 1))
    syy = MinMaxScaler(feature_range=(0, 1))
    x_train, y_train, sx, sy = train_data1(10, sx, sy, code)
    x_test, y_test, sxx, syy = test_data1(10, sx, sy, code)

    model = stock_predict(x_train, y_train, x_test, y_test, _epochs=8, _steps_per_epoch=10)
    # 7.6963124
    actual_stock_price = y_test
    print(x_test)
    print('----------------')
    predicted_stock_price = model.predict(x_test)
    actual_stock_price = syy.inverse_transform(actual_stock_price)
    predicted_stock_price = syy.inverse_transform(predicted_stock_price)
    print("--------------------")
    for i in range(len(actual_stock_price)):
        print(actual_stock_price[i], predicted_stock_price[i])
    print(actual_stock_price[-1])
    print(predicted_stock_price[-1])

    plt.plot(actual_stock_price, color='red', label='真实价格')
    plt.plot(predicted_stock_price, color='blue', label='预测价格')
    plt.xlabel('Time')
    plt.ylabel('Close Price')
    plt.legend()
    plt.show()
    return actual_stock_price, predicted_stock_price


def run_model_close(code):
    sx = MinMaxScaler(feature_range=(0, 1))
    sy = MinMaxScaler(feature_range=(0, 1))
    sxx = MinMaxScaler(feature_range=(0, 1))
    syy = MinMaxScaler(feature_range=(0, 1))
    x_train, y_train, sx, sy = train_data(10, sx, sy, code)
    x_test, y_test, sxx, syy = test_data(10, sx, sy, code)

    model = stock_predict(x_train, y_train, x_test, y_test, _epochs=8, _steps_per_epoch=10)
    # 7.6963124
    actual_stock_price = y_test
    print(x_test)
    print('----------------')
    predicted_stock_price = model.predict(x_test)
    actual_stock_price = syy.inverse_transform(actual_stock_price)
    predicted_stock_price = syy.inverse_transform(predicted_stock_price)
    print("--------------------")
    for i in range(len(actual_stock_price)):
        print(actual_stock_price[i], predicted_stock_price[i])
    print(actual_stock_price[-1])
    print(predicted_stock_price[-1])

    plt.plot(actual_stock_price, color='red', label='真实价格')
    plt.plot(predicted_stock_price, color='blue', label='预测价格')
    plt.xlabel('Time')
    plt.ylabel('Close Price')
    plt.legend()
    plt.show()
    return actual_stock_price, predicted_stock_price

def run_model(code):
    print(code)
    download_data(code)
    prepare_data(code)
    clean_data(code)
    actual_stock_open, predicted_stock_open = run_model_open(code)
    actual_stock_close, predicted_stock_close = run_model_close(code)
    return actual_stock_open, predicted_stock_open, actual_stock_close, predicted_stock_close

if __name__ == "__main__":
    run_model("600020.sh")

