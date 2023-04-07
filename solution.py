import pandas as pd
import numpy as np


chat_id = 223196602 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    ans = (x.mean() -29 + np.random.exponential(1)) / 10
    return ans # Ваш ответ
