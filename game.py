"""Игра угадай число"""

import numpy as np

number = np.random.randint(1, 101) # Zagadivaem chislo

# количество попыток
count = 0

while True:
    count+=1
    predict_number = int(input('Угадай число от 1 до 100: '))
    
    if predict_number > number:
        print('Число должгл быть меньше!')
        
    elif predict_number < number:
        print('Число должгл быть больше!')
        
    else:
        print(f'Вы угадали число! Это число = {number}, за {count} попыток')
        break # end