from pre import cls
cls()

l=[]
def f(*x):
    for c,i in enumerate(x):
        if c==0:mai=men=i
        else:
            if i>mai:mai=i
            if i<men:men=i
    print(f'Maior: {mai}\nMenor: {men}\n')

print('Valores: 1,5,6,8,9,1,2')
f(1,5,6,8,9,1,2)
