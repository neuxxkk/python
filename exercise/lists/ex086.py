from pre import cls
cls()
print(f'{"Matriz":^30}')
print('-Dimensão')
row=int(input('Linhas: '))
col=int(input('Colounas: '))

j=1
i=1
m=[]
r=[]
t=[]
s=0
ss=0
print('\n-Elemetos')
while 1:
    a=input(f'Elemento {i,j}:')
    r.append(a)
    a=int(a)
    if a%2==0:s+=a
    rr='['.join(r)
    m.append(rr)
    r.clear()
    if i==2 and j==1:
        mx=a
    elif i==2:
        if a>mx:mx=a
    if j==col :
        ss+=a
        mm=' ][ '.join(m)
        t.append(f'[ {mm} ]')
        m.clear()
        j=1
        i+=1
    else:j+=1

    if i>col:break

print('\nMatriz formatada:')
for i in range(col):
    print(t[i])
print(f'\nSoma dos elementos pares: {s}')
print(f'Soma da terceira coluna: {ss}')
print(f'Maior valor da segunda linha: {mx}\n')