"""
This file is for writing some temporary code

"""

from configparser import ConfigParser
from pathlib import Path
import os 
config_path = Path(__file__).parent / "config.ini"
assert os.path.exists(config_path) == True 
parse = ConfigParser()
parse.read(config_path, encoding="utf-8")
DAY = int(parse.get("uptrain", "DAY"))
WEEK = int(parse.get("uptrain", "WEEK"))
MONTH = int(parse.get("uptrain", "MONTH"))
Prediction_day = int(parse.get("algorithm", "PREDICTION_UP_DAY"))
print(DAY, WEEK, MONTH, Prediction_day)
