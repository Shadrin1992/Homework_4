# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.(записать в строку)
# Пример:
# k=2 => 2*x^2 + 4*x + 5 или x^2 + 5 или 10*x**2
# k=3 => 2*x^3 + 4*x^2 + 4*x + 5

from functions import create_pol_file
from functions import create_polinom

k = int(input())

print(f'Полином: {create_polinom(k)}')
create_pol_file(create_polinom(k))