from pre import cls
cls()

def f(n):
    while 1:
        print('\033[0;32;45mSISTEMA DE AJUDA\033[m')
        if n in 'FIMfimFim':break
        print('\033[0;0;42m')
        help(n)

f(input('Função ou biblioteca: '))
