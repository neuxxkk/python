from pre import cls
cls()

i=-1
n=0
s=-999
while n!=999:
    i+=1
    n=int(input(f'number{i}: '))
    s+=n

print(f'You typed {i} numbers\nThe sum between them is: {s}') 