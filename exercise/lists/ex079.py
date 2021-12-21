from pre import cls
cls()

l=[]
i=0
while 1:
    n=input(f'\nnumber{i+1}: ')
    if n=='':print('ERRO: valor inexistente')
    elif n in l:print('ERRO: valor duplicado')
    else:l.append(n)
    c=input('\nagain?[s/n]: ')    
    if c[0] in 'Nn':break    
    i+=1

print(f'\n\nLista cadastrada:')
l=', '.join(l)
print(l)
print('\n')
