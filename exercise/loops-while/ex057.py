from pre import cls
cls()

def sex():
    global n
    n=input('sexo[M/F]: ')
sex()

n=n.lower()
while n!='m' and n!='f':
    print('WRONG!')
    print('TYPE "M" OR "F"\n')
    sex()

cls()
print('Seu sexo é feminino') if n=='f' else print('Seu sexo é masculino')