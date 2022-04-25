from pathlib import Path
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

from common.eval import eval_processing

def test_eval(
            model_save_path = Path(__file__).parent / "../algo/reg/svm/save_model/toy_up_model.pickle",
            test_path = Path(__file__).parent / "../data/toy_test_up_model_20_8_3.txt",
            type:str = "reg",
            save_md_path:str = Path(__file__).parent / "../algo/reg/svm/output/metr.md" ,
            save_json_path: str = Path(__file__).parent / "../algo/reg/svm/output/metri.json" ,
            classification_threshold: list = [0,0.05],
            type_ud:str = "up",
            type_stock: str = "all"
            ):

    assert os.path.exists(model_save_path) == True
    assert os.path.exists(test_path) == True

    eval_processing(test_path,model_save_path,type,save_md_path, save_json_path, classification_threshold,type_ud, type_stock)

    assert os.path.exists(save_md_path) ==True
    assert os.path.exists(save_json_path) == True



if __name__ == "__main__":

    test_eval(Path(__file__).parent / "../algo/reg/svm/save_model/toy_up_model.pickle",
              Path(__file__).parent / "../data/toy_test_up_model_20_8_3.txt",
              "reg", Path(__file__).parent / "../algo/reg/svm/output/metr.md" , 
              Path(__file__).parent / "../algo/reg/svm/output/metri.json" , 
              [0,0.05], "up", "all")

