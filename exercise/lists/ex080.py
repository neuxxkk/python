from pre import cls
cls()

l=[]
for i in range(5):
    n=int(input(f'number{i+1}: '))
    if i==0:l.append(n)
    g=0
    for x,c in enumerate(l):
        g+=1
        if n>c:
            t=n-c
            if g==1:
                max=t
                l.insert(x+1,n)
            else:
                if t<max:l.remove(n),l.insert(x,n)
        
        if n<c:
            t=n+c
            if g==1:
                min=t
                l.insert(x,n)
            else:
                if t<min:l.remove(n),l.insert(x-1,n)
                
print(l)