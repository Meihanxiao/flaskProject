from pathlib import Path
import sys
import os
sys.path.append(os.getcwd())

from common.eval import eval_processing

def test_eval(
            model_save_path = Path(__file__)/ "../save_model/toy_up_model.h5",
            test_path = Path(__file__).parent.parent.parent / "../../data/up/test.txt",
            type:str = "reg",
            save_md_path:str = Path(__file__) / "../output/reg_gb_out.md" ,
            save_json_path: str = Path(__file__) / "../output/reg_gb_outj.json" ,
            classification_threshold: list = [0],
            type_ud:str = "up",
            type_stock: str = "all"
            ):

    assert os.path.exists(model_save_path) == True
    print(test_path)
    assert os.path.exists(test_path) == True
    output_path = Path(__file__)/ "../output"
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    eval_processing(test_path,model_save_path,type,save_md_path, save_json_path, classification_threshold,type_ud, type_stock)

    assert os.path.exists(save_md_path) ==True
    assert os.path.exists(save_json_path) == True

if __name__ == "__main__":
    test_eval()
