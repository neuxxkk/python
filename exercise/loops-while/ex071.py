from pre import cls
cls()

n=int(input('value: R$'))

def all(i):
    global n
    p=n//i
    n=n%i
    if p!=0:
        print(f'Cédulas de {i}: {p}')

all(50)
all(20)
all(10)
all(1)
