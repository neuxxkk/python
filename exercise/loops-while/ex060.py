from pre import cls
cls()

n=input('number: ')
i=int(n)
n=int(n)

r=1
f=[]
while n!=0:
    r=n*r
    n-=1
    a=n+1
    f.append(str(a))
    strF='x'.join(f)
 
print(f'{i}! = {strF} = {r}')