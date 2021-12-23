from pre import cls
cls()

max=0
min=0
px,pn='',''
fx,fn='foi','foi'
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

if len(maxn)>1:
    px='s'
    fx='foram'
if len(minn)>1:
    pn='s'
    fn='foram'

print(f'Foram cadastradas {len(l)} pessoas')
print(f'A{px} pessoa{px} mais pesada{px} {fx} {maxn} com {max}kg')
print(f'A{pn} pessoa{pn} mais leve{pn} {fn} {minn} com {min}kg')
