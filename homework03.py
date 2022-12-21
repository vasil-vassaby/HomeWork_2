# Реализуйте алгоритм перемешивания списка.
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE,
# максимум использование библиотеки Random для и получения случайного int

from random import randint

while True:
    try:
        n = int(input('Задайте кол-во элементов списка: '))
        break
    except:
        print('Задайте целое число без пробелов!')

my_list = []

for i in range(n):
    my_list.append(randint(1, 10))
print(f'Начальный список -> {my_list}')

for j in range(len(my_list)):
    index = randint(0, len(my_list) - 1)
    item = my_list.pop(index)
    my_list.append(item)
print(f'Перемешанный список -> {my_list}')