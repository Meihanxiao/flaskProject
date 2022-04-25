from pathlib import Path
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

from common.backtest import backtest

def test_for_backtest(
                    stock_list:list = ["sz.000001"],
                    start_date:str = "2000-01-01",
                    end_date:str = "2022-01-14",
                    sample_times:int = 1000,
                    type_sample:str = 'times',
                    type:str = 'reg',
                    type_ud:str = 'up',
                    model_save_path = Path(__file__).parent / "../algo/cla/svm/save_model/toy_up_model.pickle",
                    save_path: str = Path(__file__).parent / "../data/backset/down_model.txt",
                    classification_threshold: list = [0,0.05],
                    save_md_path:str = Path(__file__).parent / "../data/backtest/output/metr.md" ,
                    save_json_path: str = Path(__file__).parent / "../data/backtest/output/metri.json" ,
                    ):

    backtest_path = Path(__file__)/ "../backtest"
    if not os.path.exists(backtest_path):
        os.makedirs(backtest_path)
    data_path = Path(__file__)/ "../backtest/data"
    if not os.path.exists(data_path):
        os.makedirs(data_path)
    output_path = Path(__file__)/ "../backtest/output"
    if not os.path.exists(output_path):
        os.makedirs(output_path) 
    backtest(stock_list=stock_list,sample_times=sample_times,type_sample=type_sample,type=type,type_ud=type_ud,
            model_save_path=model_save_path,save_path=save_path,save_md_path=save_md_path,save_json_path=save_json_path)
    assert os.path.exists(model_save_path) == True
    assert os.path.exists(save_path) == True
    assert os.path.exists(save_md_path) ==True
    assert os.path.exists(save_json_path) == True


if __name__ == "__main__":
    stock_list = ["sz.000001"]
    start_date = "2000-01-01"
    end_date = "2022-01-14"
    sample_times = 10
    type_sample = 'times'
    type = 'reg'
    type_ud = 'up'
    model_save_path = Path(__file__).parent / "../algo/reg/svm/save_model/toy_up_model.pickle"
    save_path = Path(__file__) / "../backtest/data/up_model.txt"
    classification_threshold = [0,0.05]
    save_md_path = Path(__file__) / "../backtest/output/reg_up_md.md" 
    save_json_path = Path(__file__) / "../backtest/output/reg_up_j.json" 
    test_for_backtest(stock_list=stock_list,sample_times=sample_times,type_sample=type_sample,type=type,
                    type_ud=type_ud,model_save_path=model_save_path,save_path=save_path,save_md_path=save_md_path,save_json_path=save_json_path)
    
