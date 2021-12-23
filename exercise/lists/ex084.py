from pre import cls
cls()

max=0
min=0
l=[]
data=[]
while 1:
    data.append(input('Nome: '))
    data.append(int(input('Peso: ')))
    if l==[]:
        max=data[1]
        min=data[1]
        minn=[data[0]]
        maxn=[data[0]]
    else:
        if data[1]>max:
            max=data[1]
            maxn.clear()
        if data[1]<min:
            min=data[1]
            minn.clear()
        if data[1]==min:
            minn.append(data[0])
        if data[1]==max:
            maxn.append(data[0])
    l.append(data[:])
    if input('Again[s/n]: ') in 'Nn':break
    data.clear()


print()
print(f'Foram cadastradas {len(l)} pessoas')
print(f'A(s) pessoa(s) mais pesada(s) foi(ram) {maxn} com {max}kg')
print(f'A(s) pessoa(s) mais leve(s) foi(ram) {minn} com {min}kg')