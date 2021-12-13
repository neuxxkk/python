import time
from pre import cls
cls()

print('\n ALISTAMENTO')
n=int(input('birthday year: '))

y=time.localtime().tm_year
c=y-n

if c==18:print("it's time")
if c>18:print(f'passou {c-18} anos era em {y-(c-18)}')
if c<18:print(f'faltam {18-c} anos será em {y-(18-c)}')