# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint

lst = [randint(1, 7) for i in range(15)]
print(lst)
print(list(set(lst)))

lst = [i for i in lst if lst.count(i) == 1]
print(f'Список неповторяющихся элементов: {lst}')