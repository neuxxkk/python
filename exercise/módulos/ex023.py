from pre import cls
cls()

n=input('Number: ')

x=len(n)

for i in range(x):
    print(f'{i+1}º dígito: {n[i]}')