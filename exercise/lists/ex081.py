from pre import cls
cls()

five=False
l=[]
i=0
while 1:
    i+=1
    l.append(int(input(f'number{i}: ')))
    if input('Again?[s/n]: ') in 'Nn':break

l.sort(reverse=1)
if 5 in l:five=True
print(f'\nValores: {len(l)}\nDecrescente: {l}\nThere is five: {five}\n')