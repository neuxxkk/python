from random import randint
from operator import itemgetter
from pre import cls
cls()

n=int(input('How many players: '))
r={}
f={}
print('\nNames')
for i in range(n):
    name=input(f'Player {i+1}: ')
    f[f'Player {i+1}']=name.title()

for k,v in f.items():
    input(f'\n{k} roll the dice')
    d=randint(1,6)
    r[v]=d
    print(f'{v}: {d}')

rank=sorted(r.items(),key=itemgetter(1),reverse=(1))
print(f'\n{"PLACAR":^30}')
for p,w in enumerate(rank):
    print(f'{p+1}º {w[0]}')
