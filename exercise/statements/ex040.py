from pre import cls
cls()

t=0
q=int(input('how many grades: '))
x=int(input('max grade: '))
r=x*q
for i in range(q):
    n=int(input(f'nota {i+1}: '))
    t=t+n


m=t/q

if m>=r*0.60:print(f'{m}/{r} = good')
else:print(f'{m}/{r} = bad')
