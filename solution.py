import pandas as pd
import numpy as np
import statsmodels.stats.proportion


chat_id = 1943224240 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    p = 0.02
    a = statsmodels.stats.proportion.proportions_ztest(count = x_success, nobs = x_cnt, value = y_success/y_cnt, alternative='smaller')[1]
    if a <= p:
      return True
    else:
      return False
