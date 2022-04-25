from pathlib import Path
import sys
import os
sys.path.append(os.getcwd())

from common.eval import eval_processing

def test_eval(
            model_save_path = Path(__file__)/ "../save_model/20_0_0_3_train_up_model.pickle",
            test_path = Path(__file__).parent.parent.parent / "../../data/up/20_0_0_3_test_up_model.txt",
            type:str = "cla",
            save_md_path:str = Path(__file__) / "../output/cla_xg_out.md" ,
            save_json_path: str = Path(__file__) / "../output/cla_xg_outj.json" ,
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
