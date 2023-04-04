import pandas as pd
import numpy as np


chat_id = 1219503064 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    time = 93 #время по условию
    distances = x.copy() #массив с расстояниями
    distances /= ((time**2)/2) #массив с коэффициентами ускорений
    answer = distances.mean() #точечная оценка коэффициента ускорения
    return answer
