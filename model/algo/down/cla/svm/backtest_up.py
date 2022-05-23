from pathlib import Path
import sys
import os
sys.path.append(os.getcwd())

from common.backtest import backtest

def backtest_up(stock_list :list= ["sz.000001","sz.000002"],   
                sample_times:int = 1000,
                type_sample:str = 'times',
                type :str= 'cla',
                type_ud :str ='up',
                model_save_path = Path(__file__) / "../save_model/toy_up_model.pickle",
                save_path = Path(__file__) / "../backtest/up_model.txt",
                classification_threshold:list = [0,0.05],
                save_md_path:str = Path(__file__) / "../backtest/output/cla_bkt_md.md" ,
                save_json_path: str = Path(__file__) / "../data/backtest/output/cla_bkt_j.json"
                ):

    backtest_path = Path(__file__)/ "../backtest"
    if not os.path.exists(backtest_path):
        os.makedirs(backtest_path)
    output_path = Path(__file__)/ "../backtest/output"
    if not os.path.exists(output_path):
        os.makedirs(output_path)            
    

    backtest(stock_list=stock_list,sample_times=sample_times,type_sample=type_sample,type=type,model_save_path=model_save_path,
            save_path=save_path, classification_threshold=classification_threshold,type_ud=type_ud,
            save_md_path=save_md_path, save_json_path=save_json_path)

if __name__ == "__main__":
    backtest_up(stock_list = ["sz.000001","sz.000002"],   
                sample_times = 20,
                type_sample = 'times',
                type = 'cla',
                type_ud='up',
                model_save_path = Path(__file__) / "../save_model/toy_up_model.pickle",
                save_path = Path(__file__) / "../backtest/up_model.txt",
                classification_threshold = [0,0.05],
                save_md_path = Path(__file__) / "../backtest/output/cla_bkt_md.md" ,
                save_json_path = Path(__file__) / "../backtest/output/cla_bkt_j.json")
    


