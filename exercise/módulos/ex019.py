from pre import cls
cls()

import random

i=1
n=[]
for i in range(4):
    x=input(f'Nome{i}: ')
    n.append(x)

i=random.randint(1,4)

print(f'O sorteado foi {n[i]}')