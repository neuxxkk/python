from pre import cls
cls()

print(f'{"=-"*5}Tabuada{"=-"*5}\n')

while 1:
    n=input('\nnumber: ')
    if n[0]=='-':break
    n=int(n)
    for i in range(10):
        print(f'{n}x{i} = {n*i}')