from pre import cls
cls()

while 1:
    media=0
    maior=0
    mulher_vinte=0
    k=0
    for i in range(4):
        print(f'\n{"-"*5}Pessoa {i+1}{"-"*5}')
        nome=input('Nome: ')
        idade=int(input('Idade: '))
        sexo=input('Sexo[M/F]: ')

        media=media+idade

        if idade<20 and sexo.upper()[0]=='F':mulher_vinte=mulher_vinte+1

        if sexo.upper()[0]=='M':
            k=k+1
            if k==1:
                    maior=idade 
                    maior_homem=nome
            else:
                if idade>maior:maior_homem=nome
    
    media=media/4

    print(f'\n\nDatas')
    print(f'\nMedia de idade: {media:.1f}')
    print(f'Homem mais velho: {maior_homem.title()}')
    print(f'Mulheres com menos de 20 anos: {mulher_vinte}')



