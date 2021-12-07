from pre import cls
cls()

t=0
q=int(input('how many grades: '))

for i in range(q):
    n=int(input(f'nota {i+1}: '))
    t=t+n

m=t/q
print(m)