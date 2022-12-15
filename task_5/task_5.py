# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
# В file1.txt :
# 2*x**2 + 4*x + 5
# В file2.txt:
# 4*x**2 + 1*x + 4
# Результирующий файл:
# 6*x**2 + 5*x + 9

from functions import create_pol_file
from functions import create_polinom
from sympy import simplify

k = int(input())

pol1 = create_polinom(k)
pol2 = create_polinom(k)

filename1 = 'file1'
filename2 = 'file2'
sum_filename = 'sum'

create_pol_file(pol1, filename1)
create_pol_file(pol2, filename2)

with open(f'C:\\Users\\user\\Desktop\\Python Homework\\Homework_4\\task_5\\{filename1}.txt','r') as f1:
        f_pol = f1.read()
        print(f'Первый полином: {f_pol}')

with open(f'C:\\Users\\user\\Desktop\\Python Homework\\Homework_4\\task_5\\{filename2}.txt','r') as f2:
        s_pol = f2.read()
        print(f'Второй полином: {s_pol}')

sum_of_polinoms = simplify(f_pol + '+' + s_pol)
sum_of_polinoms = str(sum_of_polinoms)

with open(f'C:\\Users\\user\\Desktop\\Python Homework\\Homework_4\\task_5\\{sum_filename}.txt','w') as s:
        s.write(sum_of_polinoms)

