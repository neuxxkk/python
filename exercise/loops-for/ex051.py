from pre import cls
cls()

t=int(input('termo: '))
r=int(input('razão:'))

for i in range(10):
    if i>=t:
        print(r*i)