import sympy
from random import randint as rnd

def create_polinom(k: int, simple: bool=True):
    polinom = ''
    for i in range(k,-1,-1):
        polinom += f'{rnd(0,2)}*x**{i}+'
        if i == 0:
            polinom += f'{rnd(0,100)}'
    if simple:
        return str(sympy.simplify(polinom))
    else:
        return str(polinom)

def create_pol_file(polinon: str, filename: str='new'):
    with open(f'C:\\Users\\user\\Desktop\\Python Homework\\Homework_4\\task_4\\{filename}.txt','w') as f:
        f.write(polinon)