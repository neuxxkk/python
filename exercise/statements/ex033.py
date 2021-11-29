from pre import cls
cls()

n=[]
for i in range(3):
    n.append(int(input(f'{i+1}º number: ')))

if n[0]>n[1] and n[0]>n[2]:
    print(f'{n[0]} é o maior')
    if n[1]>n[2]:
        print(f'{n[2]} é o menor')
    else:
        print(f'{n[1]} é o menor')
elif n[1]>n[0] and n[1]>n[2]:
    print(f'{n[1]} é o maior')
    if n[0]>n[2]:
        print(f'{n[2]} é o menor')
    else:
        print(f'{n[0]} é o menor')
elif n[2]>n[0] and n[2]>n[1]:
    print(f'{n[2]} é o maior')
    if n[0]>n[1]:
        print(f'{n[1]} é o menor')
    else:
        print(f'{n[0]} é o menor')
