#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
def game_core_v2(number):
    '''Изначально берём середину отрезка в качестве предположения.
       Сокращаем отрезок в 2 раза на каждой итерации цикла.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    predict = 50
    left = 0
    right = 100
    while number != predict:
        count+=1
        if number > predict:
            left = predict
            predict = (predict + 1 + right) // 2
        elif number < predict:
            right = predict
            predict = (predict + left) // 2
    return(count) # выход из цикла, если угадали
def score_game(game_core):
    '''Запускаем 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1) #фиксируем RANDOM SEED, чтобы опыт был воспроизводим
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)
score_game(game_core_v2)


# In[ ]:




