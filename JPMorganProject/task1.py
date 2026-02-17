import math
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt 
#from datetime import datetime, timedelta
#import numpy as np


data =yf.download("NG=F", start="2022-01-01")
print(data.head())

