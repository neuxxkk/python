from pre import cls
cls()

x='atletico','flamengo','palmeiras','bahia','cruzeiro'

for y,i in enumerate(x):
    if i=='bahia':b=y

print(f'Tabela: {x}')
print(f'\nG2: {x[:2]}')
print(f'\nLanternas: {x[-2:]}')
print(f'\nOrdem alfabetica: {sorted(x)}')
print(f'\nBahia está em: {b+1}º')