import numpy as np 
from sklearn import metrics

def calculate_acc(golden_y: list = np.array([1,2,3,1]), prediction_y: list = np.array([1,2,3,3])) -> float:

    assert len(golden_y) == len(prediction_y), "golden_y must has the same length with prediction_y"
    assert isinstance(golden_y, np.ndarray)
    assert isinstance(prediction_y, np.ndarray)

    acc = np.mean(np.equal(prediction_y, golden_y))
    return round(acc, 4)

def calculate_recall(golden_y: list = np.array([1,2,3,1]), prediction_y: list = np.array([1,2,3,3])) -> float:

    assert len(golden_y) == len(prediction_y), "golden_y must has the same length with prediction_y"
    assert isinstance(golden_y, np.ndarray)
    assert isinstance(prediction_y, np.ndarray)

    rec = metrics.recall_score(golden_y, prediction_y, average='macro')
    return round(rec, 4)

def calculate_single_label_recall(golden_y: list = np.array([1,2,3,1]), prediction_y: list = np.array([1,2,3,3]),label: int = 1) -> float:

    assert len(golden_y) == len(prediction_y), "golden_y must has the same length with prediction_y"
    assert isinstance(golden_y, np.ndarray)
    assert isinstance(prediction_y, np.ndarray)

    sin_rec = metrics.recall_score(golden_y, prediction_y, average=None)
    return round(sin_rec[label-1], 4)

def calculate_precision(golden_y: list = np.array([1,2,3,1]), prediction_y: list = np.array([1,2,3,3])) -> float:

    assert len(golden_y) == len(prediction_y), "golden_y must has the same length with prediction_y"
    assert isinstance(golden_y, np.ndarray)
    assert isinstance(prediction_y, np.ndarray)

    pre = metrics.precision_score(golden_y, prediction_y, average='macro')
    return round(pre, 4)

def calculate_single_precision(golden_y: list = np.array([1,2,3,1]), prediction_y: list = np.array([1,2,3,3]),label: int = 1) -> float:

    assert len(golden_y) == len(prediction_y), "golden_y must has the same length with prediction_y"
    assert isinstance(golden_y, np.ndarray)
    assert isinstance(prediction_y, np.ndarray)

    sin_pre = metrics.precision_score(golden_y, prediction_y, average=None)
    return round(sin_pre[label-1], 4)

def calculate_f1(golden_y: list = np.array([1,2,3,1]), prediction_y: list = np.array([1,2,3,3])) -> float:

    assert len(golden_y) == len(prediction_y), "golden_y must has the same length with prediction_y"
    assert isinstance(golden_y, np.ndarray)
    assert isinstance(prediction_y, np.ndarray)

    f1 = metrics.f1_score(golden_y, prediction_y, average='macro')
    return round(f1, 4)

def calculate_single_f1(golden_y: list = np.array([1,2,3,1]), prediction_y: list = np.array([1,2,3,3]),label: int = 1) -> float:

    assert len(golden_y) == len(prediction_y), "golden_y must has the same length with prediction_y"
    assert isinstance(golden_y, np.ndarray)
    assert isinstance(prediction_y, np.ndarray)

    sin_f1 = metrics.f1_score(golden_y, prediction_y, average=None)
    return round(sin_f1[label-1], 4)

def calculate_evs(golden_y: list = np.array([1,2,3,1]), prediction_y: list = np.array([1,2,3,3])) -> float:
    
    return round(metrics.explained_variance_score(golden_y, prediction_y), 4)

def calculate_mae(golden_y: list = np.array([1,2,3,1]), prediction_y: list = np.array([1,2,3,3])) -> float:
    
    return round(metrics.mean_absolute_error(golden_y, prediction_y), 4)

def calculate_mse(golden_y: list = np.array([1,2,3,1]), prediction_y: list = np.array([1,2,3,3])) -> float:
    
    return round(metrics.mean_squared_error(golden_y, prediction_y), 4)

def calculate_medae(golden_y: list = np.array([1,2,3,1]), prediction_y: list = np.array([1,2,3,3])) -> float:
    
    return round(metrics.median_absolute_error(golden_y, prediction_y), 4)

def calculate_r2(golden_y: list = np.array([1,2,3,1]), prediction_y: list = np.array([1,2,3,3])) -> float:
    
    return round(metrics.r2_score(golden_y, prediction_y), 4)
