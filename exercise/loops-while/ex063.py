from pre import cls
cls()


print(f'{"-"*5}Fibonacci{"-"*5}\n')
n=int(input('How many terms: '))
f=[0,1,1]
i=3
while i<n:
    add=f[len(f)-2]+f[len(f)-1]
    f.append(add)
    i+=1
        
print(f)