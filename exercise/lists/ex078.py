from pre import cls
cls()

l=[]
for i in range(5):
    n=int(input(f'number{i+1}: '))
    l.append(str(n))
    if i==0:
        max=    min=(n,i+1)
    else:
        if n>max[0]:max=(n,i+1)
        if n<min[0]:min=(n,i+1)

l=', '.join(l)
print(f'\nValores: {l}')
print(f'\nmax: {max[0]}\npos: {max[1]}º\n\nmin: {min[0]}\npos: {min[1]}º')

