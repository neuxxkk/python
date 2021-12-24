from random import randint
from pre import cls
cls()

l=[]
x=[]
print(f'{"Mega Sena":^30}')
n=int(input('Quantos jogos: '))
print()
for i in range(n):
    for c in range(6):x.append(str(randint(1,60)))
    x=', '.join(x)
    l.append((f'Jogo {i+1}: ',x[:],'\n'))
    x=[]
    l[i]=''.join(l[i])
    print(l[i])


