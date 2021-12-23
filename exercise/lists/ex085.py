from pre import cls
cls()

l=[[],[],]
for i in range(7):
    n=int(input(f'Number{i+1}: '))
    l[0].append(n) if n%2==0 else l[1].append(n)

def f(x):
    if x!=[]:
        x.sort()
    else:x=='non'

f(l[0])
f(l[1])

print(f'Pairs: {l[0]}')
print(f'Odds: {l[1]}')