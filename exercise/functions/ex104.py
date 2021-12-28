from pre import cls
cls()

def f(n):
    while 1:
        x=input(n)
        if not x.isnumeric():print('\033[0;31mERRO: Digite um número inteiro válido\033[m')
        else:break
    return x

y=f('Digite um número: ')
print(f'Number typed: {y}')