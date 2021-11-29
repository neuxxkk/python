from pre import cls
cls()

n=int(input('Velocidade: '))

if n>80:
    m=n-80
    print(f'multa de ${m*7}')
else:
    print('ok')