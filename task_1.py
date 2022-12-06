# 1. Задайте список, состоящий из произвольных чисел,
#  количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов
#  списка, стоящих на нечётных позициях(не индексах).
# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22
# in
# 4
# out
# [4, 2, 4, 9]
# 8

def sum(list1):
    sum = 0
    for i in range (0, len(list1), 2):
        sum += list1[i]
    return sum
from random import sample
list = sample (range(1, 10), k = int(input('Введите кол-во:, ')))

result = sum(list)
print(list)
print(f'Сумма элементов, стоящих на нечетной позиции = {result}')