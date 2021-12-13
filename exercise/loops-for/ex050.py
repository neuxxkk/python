from pre import cls
cls()

f=0
for i in range(6):
    n=int(input(f'number{i+1} :'))
    if n%2==0:
        f=f+n

print(f'\n{f}')