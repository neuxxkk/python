from pre import cls
cls()


n=int(input('value: R$'))

print('1- a vista\n2- a vista cartao\n3- 2x cartao\n4- 3x cartao')
c=int(input())

if c==1:n=n-(n*0.10)  
if c==2:n=n-(n*0.05)
if c==4:n=n+(n*0.20)

print(f'\nR${n}')