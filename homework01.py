# Напишите программу, которая
# принимает на вход вещественное число
# и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

while True:
    try:
        number = float(input('Введите число: '))
        break
    except:
        print('Введите вещественное число!')

print(number)