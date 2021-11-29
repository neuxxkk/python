from pre import cls
cls()

n=[]
for i in range(3):
    n.append(float(input(f'Lado {i+1}: ')))

b1=n[1]+n[2]>n[0]
b2=n[0]+n[2]>n[1]
b3=n[0]+n[1]>n[2]

if b1 and b2 and b3:
    print('Triangle done')
else:
    print("You can't do triamgle")