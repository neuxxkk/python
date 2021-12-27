#100 ceeemmmm
from random import randint
from pre import cls
cls()

def f():
    l=[]
    p=0
    for i in range(5):
        x=randint(0,10)
        l.append(x)
        p+=x if x%2==0 else 0
    print(f'\nValores: {l}\nSoma dos pares: {p}\n')
f()


def rand(x):
    for i in range(5):
        x.append(randint(0,10))

def pair_s(y):
    p=0
    for i in y:
        if i%2==0:p+=i
    print(f'\nValores: {y}\nSoma dos pares: {p}\n')
l=[]
rand(l)
pair_s(l)