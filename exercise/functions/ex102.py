from pre import cls
cls()
while 1:
    def f(x,s=0):
        """
        Calcula o fatorial de x
        x: número a se calcular faatorial
        s: literal sobre mostrar ou não cáuculo
        """
        y=1
        for i in range(x,0,-1):
            print(i,end='')
            y*=i
            if s:print(' x ',end='') if i!=1 else print(' = ',end='')
        return y

    x=int(input('Fatorial de: '))
    s=input('Show calc?[Y/N]: ')

    print(f(x)) if s in 'Nn' else print(f(x,1))
    if input('\nNeed help?[Y/N]: ') in 'YySs':help(f)
    if input('\nAgain?[Y/N]: ') in 'Nn':break 
    else:cls()


