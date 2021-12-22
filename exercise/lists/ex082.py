from pre import cls
cls()

i=0
l,lp,lo=[],[],[]
while 1:
    i+=1
    l.append(int(input(f'number{i}: ')))
    if input('Again?[s/n]: ') in 'Nn':break

for v in l:
    lp.append(v) if v%2==0 else lo.append(v)

print(f'\nList: {l}')
print(f'Odd list: {lo}')
print(f'Pair list: {lp}\n')