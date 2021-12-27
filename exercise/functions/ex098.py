from pre import cls
cls()

def f(s,e,t):
    sf=s
    print('\nCrescente: ')
    while sf<e:
        sf+=t
        print(sf,end=' ')        
    ef=e
    print('\nDecrescente: ')
    while ef>s:
        ef-=t
        print(ef,end=' ')
        
        
s=int(input('Start: '))
e=int(input('End: '))
t=int(input('Step: '))
f(s,e,t)