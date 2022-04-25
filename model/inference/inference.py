import json

def model_analysis(stock_code: str = "sh.600000"):
    """
    stock_code: 是股票代码，比如 “sh.600000”，如果 = all，说明模型是给所有股票使用的
    score：模型预测的分数
    type：“up” 说明是预测涨的模型，“down” 说明是预测跌的模型
    version: 模型版本号
    author：模型开发作者
    """
    
    dict = {"stock_code": "all", "score": 0.9, "type": "up", "version": "20220228", "author": "yefei"}
    return json.dumps(dict)
