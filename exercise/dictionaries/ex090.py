from pre import cls
cls()   

nome=input('Nome: ')
media=float(input('Média: '))

l={
    nome:media
}

status='Recuperação' if media<6 and media>4 else 'Aprovado'

for n,m in l.items():
    print(f'\nNome: {n}')
    print(f'Média: {m}')
    print(f'Status: {status}\n')
