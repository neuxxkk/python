from random import choice, randint
from pre import cls
cls()

win=1
i=0
while win:
    print()
    player=input('Your name: ')
    player_c=input('even or odd: ')
    pc_c='odd' if player_c[0].title()=='o' else 'even'

    print(f'\nPC: {pc_c}\n{player.upper()}: {player_c}\n')

    pc_n=randint(0,10)
    player_n=int(input('number: '))
    r=player_n+pc_n

    print(f'\nPC: {pc_n}\n{player.upper()}: {player_n}\n')

    win=1 if r%2==0 and pc_c=='odd' else 0