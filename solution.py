import pandas as pd
import numpy as np


chat_id = 1219503064 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    time = 93
    distances = x.copy()
    distances /= ((93**2)/2)
    answer = distances.mean()
    return answer
