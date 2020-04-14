'''В функции game_core_bi реализован алгоритм бинарного поиска. 
В среднем алгоритм угадывает число за 5 попыток.'''
import numpy as np
#number = np.random.randint(1, 101)
def game_core_bi(number):
    count = 0
    aa = 1
    ab = 101
    while True:
        rr = range(aa, ab)
        predict = rr[int(len(rr) / 2) - 1]
        count += 1
        if number == predict: break
        elif number > predict:
            aa = predict + 1
        elif number < predict:
            ab = predict
    return(count)
def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    #np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000)) #класс объекта нумпай массив
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    #print(count_ls)
    #print(random_array)
    #return(score)
#game_core_bi(number)
score_game(game_core_bi)