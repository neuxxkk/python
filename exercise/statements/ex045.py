from random import choice
from pre import cls
cls()

c={
    1:'tesoura',
    2:'pedra',
    3:'papel'
}
i=0
f=False
print(f'{" "*10}Jokenpô\n')
pc_n=choice([c[1],c[2],c[3]])
u_n=input('pick one: ')

print(f'\nPC: {pc_n}\nUSER: {u_n}')

if pc_n==c[1]:
    if u_n==c[3]:
        f='lose'
    if u_n==c[2]:
        f='win'
    if u_n==c[1]:
        f='draw'
elif pc_n==c[2]:
    if u_n==c[3]:
        f='win'
    if u_n==c[2]:
        f='draw'
    if u_n==c[1]:
        f='lose'
elif pc_n==c[3]:
    if u_n==c[3]:
        f='draw'
    if u_n==c[2]:
        f='lose'
    if u_n==c[1]:
        f='win'

if not f:i=1,print('TYPE: "pedra", "papel" ou "tesoura"')

if i==0:
    print(f'\n{" "*10}YOU {f.upper()}')

