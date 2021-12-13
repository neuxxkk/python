from pre import cls
cls()

n=int(input('number: '))
f=0
p=0
for i in range(10):
    if i!=1 and i!=0 and n%i==0:
        p+=1
        f=1

print(f'{n} is primo') if f!=1 else print(f'{n} is not primo divisível {p} vezes')
