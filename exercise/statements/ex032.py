from pre import cls 
cls()

n=int(input('Year: '))

if n%4==0:
    if n%100==0 and n%400!=0:
        print(f'{n} não é bissexto')
    else:
        print(f'{n} é bissexto')
else:
    print(f'{n} não é bissexto')