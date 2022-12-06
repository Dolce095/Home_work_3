# 2. Напишите программу, которая найдёт произведение 
# пар чисел списка.
# Парой считаем первый и последний элемент, второй
#  и предпоследний и т.д.
# in
# 4
# out
# [2, 5, 8, 10]
# [20, 40]
# in
# 5
# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]

def pari(list):
    list1 = []
    count = -1
    i = 0
    lenf = len(list) / 2
    while i < lenf:
        list1.append(list[i]*list[count])
        count -= 1
        i += 1
    return list1


from random import sample
list = sample (range(1, 10), k = int(input('Введите кол-во:, ')))
list1 = pari(list)
print(list)
print(list1)
