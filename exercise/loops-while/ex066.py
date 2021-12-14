from pre import cls
cls()

i=0
n=0
s=0
while 1:
    i+=1
    n=int(input(f'number{i}: '))
    if n==999:
        break
    s+=n


print(f'You typed {i} numbers\nThe sum between them is: {s}') 