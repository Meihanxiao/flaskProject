import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

from common.metrics import calculate_acc
from common.metrics import calculate_recall
from common.metrics import calculate_single_label_recall
from common.metrics import calculate_precision
from common.metrics import calculate_single_precision
from common.metrics import calculate_f1
from common.metrics import calculate_evs
from common.metrics import calculate_mae
from common.metrics import calculate_mse
from common.metrics import calculate_medae
from common.metrics import calculate_r2
from common.metrics import calculate_single_f1

if __name__ == "__main__":
   print(calculate_acc())
   print(calculate_recall())
   print(calculate_single_label_recall())
   print(calculate_precision())
   print(calculate_single_precision())
   print(calculate_f1())
   print(calculate_single_f1())
   print(calculate_evs())
   print(calculate_mae())
   print(calculate_mse())
   print(calculate_medae())
   print(calculate_r2())


