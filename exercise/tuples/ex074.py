from random import randint
from pre import cls
cls()

a=randint(0,10)
b=randint(0,10)
c=randint(0,10)
d=randint(0,10)
e=randint(0,10)

n=(a,b,c,d,e)  

for i in range(len(n)):
    if i==0:
        max=n[i]
        min=n[i]
    else:
        if n[i]>max:max=n[i]
        if n[i]<min:min=n[i]

print(f'numbers: {n}')
print(f'maior: {max}\nmenor: {min}')