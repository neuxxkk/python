from pre import cls

c='y'

while c[0].upper()=='Y':
    cls()
    print(f'{"-="*5}Calculator{"-="*5}')
    print(f'{" "*8}[999 to stop]{" "*10}\n')
    i=0
    t=0
    max=0
    min=0
    n=int(input(f'number{i+1}: '))

    while n!=999:
        i+=1
        t+=n
        if i==1:
            max=n
            min=n
        elif i>0:
            if n>max:max=n
            if n<min:min=n

        n=int(input(f'number{i+1}: '))

    avr=t/i
    print(f'\nAverage: {avr:.2f}\nBiggest value: {max}\nSmallest value: {min}')
    c=input('\nAgain?:')