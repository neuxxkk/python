from pre import cls
cls()

termo=int(input('termo: '))
razao=int(input('razão: '))
quantia=10
pa=termo+razao
i=0
q=1

while i<quantia:
    print(pa)
    pa+=razao
    i+=1

while q>0:
    print('PAUSA\n')
    q=int(input('quantos mais: '))
    quantia+=q

    while i<quantia:
        print(pa)
        pa+=razao
        i+=1




