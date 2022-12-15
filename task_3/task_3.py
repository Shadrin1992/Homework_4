# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint

lst = [randint(1, 5) for i in range(15)]
print(lst)

print(list(set(lst)))