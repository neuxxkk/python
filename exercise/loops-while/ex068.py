from random import choice, randint
from pre import cls
cls()

win=1
i=0
player=input('Your name: ')

while 1:
    print()
    player_c=input('even or odd: ')
    pc_c='odd' if player_c[0].title()!='O' else 'even'

    print(f'\nPC: {pc_c}\n{player.upper()}: {player_c}\n')

    pc_n=randint(0,10)
    player_n=int(input('number: '))
    r=player_n+pc_n

    print(f'\nPC: {pc_n}\n{player.upper()}: {player_n}\n')

                        


    if r%2==0 and pc_c=='odd'or r%2!=0 and pc_c=='even':
        print(f'\nResult: {r} - even') if r%2==0 else     print(f'\nResult: {r} - odd')
        i+=1
        print(f'{"-"*5}You win{"-"*5}')
    else:
        print(f'{"-"*5}You lose{"-"*5}\n\nPoints: {i}')
        break