from pre import cls 
cls()

g=[]
t=0
e=0
r={}
l=[]
while 1:
    e+=1
    t=0
    g.clear()
    n=input('\nNome: ')
    p=int(input('Partidas jogadas: '))
    for i in range(p):
        gi=int(input(f'  Gols na {i+1}º partida: '))
        t+=gi
        g.append(gi)
    r['id']=e
    r['name']=n
    r['goals']=g[:]
    r['total']=t
    l.append(r.copy())
    if input('\nContinuar[s/n]: ') in 'Nn':break

print()
print(l)

print()
print('Id     Name     Gols          Total')
for i in l:
    for k,v in i.items():
        if k=='id':print(f'{str(v):<7}',end='')
        if k=='name':print(f'{str(v):<9}',end='')
        if k=='goals':print(f'{str(v):<16}',end='')
        if k=='total':print(f'{v}',end='')
    print()
print()
while 1:
    id=int(input('Mostrar dados de qual jogador[Id/999=stop]: '))
    if id==999:break
    for i in l:
        if i['id']==id:
            for k, v in i.items():print(f'{k}: {v}')

