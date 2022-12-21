# Задайте список из n чисел последовательности (1 + 1/n)^n,
# выведеите его на экран,
# а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

import random
while True:
    try:
        n = int(input('Задайте число n: '))
        break
    except:
        print('Задайте целое число без пробелов!')

my_list = []

for i in range(1, n + 1):
    my_list.append(round((1 + 1/i)**i, 2))

print(f'Список из {n} чисел -> {my_list}')

sum = 0

for j in range(len(my_list)):
    sum += my_list[j]

print(f'Сумма чисел = {sum}')