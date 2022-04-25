from pathlib import Path
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

from inference.inference import model_analysis

data = model_analysis()
print(data)