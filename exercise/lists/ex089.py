from pre import cls
cls()

aluno=[]
boletim=[]
data=[]
i=0
while 1:
    i+=1
    name=input('Name: ')
    n1=int(input('Nota 1: '))
    n2=int(input('Nota 2: '))
    m=(n1+n2)/2
    data.append(f'{name}: {n1,n2}')
    aluno.append(f'{name.title()}: {str(m)}')
    a=', '.join(aluno[:])
    boletim.append(a)
    aluno.clear()
    if input('Again[s/n]: ') in 'Nn':break

print()
for c in range(i):
 print(boletim[c])
print()

while 1:
    show=input('Show someone especific?[name/no]: ')
    if show in 'Nono':break
    for i in data:
        if show.lower() in i:print(i)