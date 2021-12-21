from pre import cls
cls()

print(f'{"Vogais":^30}\n')
n=('celular','televisão','mouse','computador','caderno')

for i in n:
    v=[]
    for c in i:
        if c in 'aeiou':v.append(c) 
    v=', '.join(v) 
    print(f'{i}: {v}')
