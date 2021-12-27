from pre import cls
cls()

data={}
g=0
m=[]
l=[]
ac=[]
while 1:
    data['name']=input('Name: ')
    while 1:
        s=input('Sexo[F/M]: ')
        if s in 'Mm' or s in 'Ff':
            data['sex']='Masculino' if s in 'Mm' else 'Feminino'
            break
        print('ERRO: somente M ou F')
    data['age']=int(input('Idade: '))
    g+=data['age']
    l.append(data.copy())
    while 1:
        c=input('\nMore[s/n]: ')
        if c in 'Nn' or c in 'Ss':
            if c in 'Nn':c=1
            break
        print('ERRO: somente S ou N')
    if c==1:break

A=len(l)
B=g/len(l)

for i in l:
    if i['sex'] in 'Mm':m.append(i['name'])
    if i['age']>B:ac.append(i)



C=m
D=ac

print()
print(f'Pessoas casdastradas: {A}')
print(f'Média de idade: {B:.2f}')
print(f'Mulheres cadastradas: {C}')
print(f'Pessoas acima da média:')
for i in D:
    for k,v in i.items():
        print(f' {k}= {v}; ',end='')
    print()