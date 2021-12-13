from pre import cls
cls()

q=0
n=0
for i in range(500):
    if i%3==0 and i%2==0:
        q=q+1
        n=n+i

print(q)
print(n)
