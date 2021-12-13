from pre import cls
cls()

t=int(input('termo: '))
r=int(input('razão: '))

for i in range(10):
    if i==0:
        pa=t+r
    else:pa+=r
    print(pa)