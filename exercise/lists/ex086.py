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
print('\n-Elemetos')
while 1:
    a=input(f'Elemento {i,j}:')
    r.append(a)
    rr='['.join(r)
    m.append(rr)
    r.clear()
    if j==col :
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
print()