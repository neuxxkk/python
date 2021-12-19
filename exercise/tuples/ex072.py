from pre import cls
cls()

while 1:
    n=int(input('number[0 - 10]: '))

    x='um','dois','três','quatro','cinco','seis','sete','oito','nove','dez'

    if 10>= n >=0:
        print(f'number {x[n-1]}')
        break
    