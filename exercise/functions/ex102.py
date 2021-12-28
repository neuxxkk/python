from pre import cls
cls()
while 1:
    def f(x,s):
        """Calcula o fatorial de x
            x: número a se calcular faatorial
            s: literal sobre mostrar ou não cáuculo"""
        f=x
        if s:print(x,end=' x ')
        for i in range(1,x):
            f*=i
            if s:print(x-i,end=f' = {f}') if x-i==1 else print(x-i,end=' x ')
        if not s:print('\n',f)

    x=int(input('Fatorial de: '))
    s=input('Show calc?[Y/N]: ')

    f(x,0) if s in 'Nn' else f(x,1)
    if input('\nNeed help?[Y/N]: ') in 'YySs':help(f)
    if input('\nAgain?[Y/N]: ') in 'Nn':break 
    else:cls()


