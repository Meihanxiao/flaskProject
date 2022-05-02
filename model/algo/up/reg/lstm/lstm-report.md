
# 问题描述

在该问题中，我们主要是解决的是利用股票前20天的量价数据，结合深度学习的模型来预测未来三天的股票涨辐。  

# 数据分析

数据（包括股票的收盘价，开盘价，最高价，最低价，成交量，换手率以及涨跌幅）

```
sz.300127,2016-12-13,0.0157,15.64,15.92,14.94,15.34,6849261.0,3.1,-3.63
```

以此条数据为例，依次代表了股票代码(stock_code)，该条数据的时间，在预测时段的实际涨跌幅，开盘价(open)，最高价(high)，最低价(low)，收盘价(close)，成交量(volume)，换手率(turn)以及当日涨跌幅(pctChg)。

对于预测时段实际涨幅大于0的股票的标签记作1，将涨幅小于0的股票的标签记为2。同时，在训练数据中，两种标签的数据分别有325条。在测试数据中，两种标签的数据分别有75条。
训练数据与测试数据均存放于/data/up/下

分析结果可得，xgboost的准确率最低，为0.58，randomforest的准确率最高，为0.64.随机森林的测试结果为标签为1的样本有82个，标签为2的样本有68个。



![标签分布]( files/1.png)




# 模型分析

## gb模型

### 模型架构

GBDT是一种迭代的决策树算法，由多棵决策树组成，所有树的结论累加起来作为最终答案。通过梯度下降来对新的学习器进行迭代。而GBDT中采用的就是CART决策树。
输入为带有325个标签0和带有325个标签1的股票数据，输出结果为训练完的模型。

### 代码

```
def gb_process(
                train_path: str = Path(__file__).parent.parent.parent / "../data/toy_train_up_model_20_8_3.txt", 
                model_save_path: str = Path(__file__).parent / "save_model/toy_up_model.pickle",
                classification_threshold: list = [0,0.05],
                type:str = "cla",
                n:float = 100
                ):
    
    train_data_set_x, train_data_set_y = read_up_dataset(train_path, classification_threshold, type)
    
    debug = 0
    if debug == 0:
        train_x, train_y = [], []
        label_num = []
        for i in range (len(classification_threshold)+2):
            label_num .append(325)
      #  print(label_num)
     #   two = 325
      #  one = 325   # lable = 1 的数量
        for i in range(len(train_data_set_y)):
            if label_num[train_data_set_y[i]] >0:
                label_num[train_data_set_y[i]]-=1
                train_x.append(train_data_set_x[i])
                train_y.append(train_data_set_y[i])
            
        train_data_set_x = np.array(train_x)
        train_data_set_y = np.array(train_y)


    if debug==1:
        print(train_data_set_y)
        stat = {}
        for item in train_data_set_y:
            if item not in stat:
                stat[item] = 1
            else:
                stat[item] += 1
        print(stat)
        

    # do some post processing here
    #train_data_set_x = post_processing(train_data_set_x)
 

    clf = GradientBoostingClassifier(learning_rate=0.1,n_estimators=60,max_depth=4,random_state=n).fit(train_data_set_x, train_data_set_y)

    with open(model_save_path,'wb') as f: 
        pickle.dump(clf,f)
```

### 实验结果

首先调整learning_rate
| learning_rate | 0.1 | 0.2 |0.3| 0.4| 0.5 | 0.6 |0.7| 0.8| 0.9 | 1|
| :--------:    | :----:| :---: | :---: |:----: |:----:| :-----: | :----: |:----: | :----: |:----: |
| ac率 | 0.5733 |0.54|0.5533| 0.5067| 0.4467|0.52|0.54| 0.5133|0.54| 0.5067|

将 learning_rate设定为0.1 

对n_estimators 进行调参 
|n_estimators  | 10 | 20 |30| 40| 50 | 60 |70| 80| 90 | 100|
| :--------:    | :----:| :---: | :---: |:----: |:----:| :-----: | :----: |:----: | :----: |:----: |
| ac率 | 0.5667 |0.56|0.5333| 0.5467| 0.5733|0.6067|0.5733| 0.6|0.5533| 0.5667|

n_estimators = 60时较好

开始对决策树进行调参。首先对决策树最大深度max_depth进行网格搜索

|max_depth  | 1 | 2 |3| 4| 5 | 6 |7| 8| 9 | 10|
| :--------:    | :----:| :---: | :---: |:----: |:----:| :-----: | :----: |:----: | :----: |:----: |
| ac率 | 0.5667 |0.5467|0.6| 0.6067| 0.5733|0.56|0.6| 0.5467|0.5667| 0.4867|

当max_depth = 4时较好

| learning_rate | n_estimators | max_depth |random_state| ac率|
| :--------:    | :-----------:| :-------: | :-------: |:-------: |
| 0.1 | 60 |4|0| 0.6|


## XGBOOST模型

### 模型架构
XGBoost）是基于Boosting框架的一个算法工具包（包括工程实现），在并行计算效率、缺失值处理、预测性能上都非常强大。xgboost与GBDT较为类似。
输入为带有325个标签0和带有325个标签1的股票数据，输出结果为训练完的模型。

### 代码

```
def xgboost(
                train_path: str = Path(__file__).parent.parent.parent / "../data/toy_train_up_model_20_8_3.txt", 
                model_save_path: str = Path(__file__).parent / "save_model/toy_up_model.pickle",
                classification_threshold: list = [0,0.05],
                type:str = "cla",
                n:float = 100
                ):
    
    train_data_set_x, train_data_set_y = read_up_dataset(train_path, classification_threshold, type)
    
    debug = 0
    if debug == 0:
        train_x, train_y = [], []
        label_num = []
        for i in range (len(classification_threshold)+2):
            label_num .append(325)
      #  print(label_num)
     #   two = 325
      #  one = 325   # lable = 1 的数量
        for i in range(len(train_data_set_y)):
            if label_num[train_data_set_y[i]] >0:
                label_num[train_data_set_y[i]]-=1
                train_x.append(train_data_set_x[i])
                train_y.append(train_data_set_y[i])
            
        train_data_set_x = np.array(train_x)
        train_data_set_y = np.array(train_y)


    if debug==1:
        print(train_data_set_y)
        stat = {}
        for item in train_data_set_y:
            if item not in stat:
                stat[item] = 1
            else:
                stat[item] += 1
        print(stat)
        

    # do some post processing here
    #train_data_set_x = post_processing(train_data_set_x)

    

    clf = XGBClassifier(n_estimators=n,random_state = 90,max_depth = n).fit(train_data_set_x, train_data_set_y)

    with open(model_save_path,'wb') as f: 
        pickle.dump(clf,f)
```

### 实验结果

首先对n_estimators 进行调参 数据如下
|n_estimators  | 200 | 210 |220| 230| 240 | 250 |260| 270| 280 | 290|
| :--------:    | :----:| :---: | :---: |:----: |:----:| :-----: | :----: |:----: | :----: |:----: |
| ac率 | 0.5667|0.5467|0.5533| 0.56| 0.56|0.5533|0.5667| 0.5733|0.58| 0.58|

接下来对max——depth进行调参，当其为3时准确率在0.58左右
|max_depth  | 1 | 2 |3| 4| 5 | 6 |7| 8| 9 |
| :--------:    | :----:| :---: | :---: |:----: |:----:| :-----: | :----: |:----: | :----: |
| ac率 | 0.5067 |0.54|0.56| 0.5733| 0.58|0.54|0.5667| 0.4933|0.5533|

| n_estimators | max_depth | ac率|
| :-----------:| :-------: |:-------: |
| 280 |5| 0.58|

## RandomForest模型

### 模型架构
随机森林即由多个决策树组成，每个决策树并不相同，在构建决策树时，我们从训练数据中有放回的随机选取一部分样本，并且也不会使用数据的全部特征，而是随机选取部分特征进行训练。每棵树使用的样本和特征都不相同，训练出的结果也不相同。

输入为带有325个标签0和带有325个标签1的股票数据，输出结果为训练完的模型。

### 代码

```
def RandomForest_process(
                train_path: str = Path(__file__).parent.parent.parent / "../data/toy_train_up_model_20_8_3.txt", 
                model_save_path: str = Path(__file__).parent / "save_model/toy_up_model.pickle",
                classification_threshold: list = [0,0.05],
                type:str = "cla",
                n:float = 100
                ):
    
    train_data_set_x, train_data_set_y = read_up_dataset(train_path, classification_threshold, type)
    
    debug = 0
    if debug == 0:
        train_x, train_y = [], []
        label_num = []
        for i in range (len(classification_threshold)+2):
            label_num .append(325)
        print(label_num)
     #   two = 325
      #  one = 325   # lable = 1 的数量
        for i in range(len(train_data_set_y)):
            if label_num[train_data_set_y[i]] >0:
                label_num[train_data_set_y[i]]-=1
                train_x.append(train_data_set_x[i])
                train_y.append(train_data_set_y[i])
            
        train_data_set_x = np.array(train_x)
        train_data_set_y = np.array(train_y)


    if debug==1:
        print(train_data_set_y)
        stat = {}
        for item in train_data_set_y:
            if item not in stat:
                stat[item] = 1
            else:
                stat[item] += 1
        print(stat)
        

    # do some post processing here
    #train_data_set_x = post_processing(train_data_set_x)

    

    clf = RandomForestClassifier(n_estimators=85,random_state=90,max_depth=n).fit(train_data_set_x, train_data_set_y)

    with open(model_save_path,'wb') as f: 
        pickle.dump(clf,f)
```

### 实验结果

首先对n_estimators进行调整， 80左右时准确率较高 ，对80——90进行测试，发现在85时准确率最高

对n_estimators 进行调参 数据如下
|n_estimators  | 30 | 40 |50| 60| 70 | 80 |90| 100| 110 | 120|
| :--------:    | :----:| :---: | :---: |:----: |:----:| :-----: | :----: |:----: | :----: |:----: |
| ac率 | 0.58 |0.58|0.56| 0.5867| 0.5933|0.6133|0.5933| 0.62|0.6133| 0.6067|

|n_estimators  | 80 | 81 |82| 83| 84 | 85 |86| 87| 88 | 89|
| :--------:    | :----:| :---: | :---: |:----: |:----:| :-----: | :----: |:----: | :----: |:----: |
| ac率 | 0.6133 |0.6267|0.62| 0.6067| 0.6267|0.6333|0.6267| 0.6|0.6067| 0.5933|

下来对max_depth进行调参，7时准确率较高。
|max_depth  | 1 | 2 |3| 4| 5 | 6 |7| 8| 9 | 10|
| :--------:    | :----:| :---: | :---: |:----: |:----:| :-----: | :----: |:----: | :----: |:----: |
| ac率 | 0.5667 |0.5533|0.5667| 0.6067| 0.5867|0.58|0.64| 0.6|0.6| 0.5667|

此时 准确率在0.64左右。
| n_estimators | max_depth |random_state| ac率|
| :-----------:| :-------: | :-------: |:-------: |
| 85 |7|90| 0.64|
