from pre import cls
cls()

def f(j='<desconhecido>',g=0):
    print(f'O jogador {j} fez {g} gol(s)')

t=input('Nome do jogador: ')
n=input('Número de gols: ')

try:n=int(n)
except:n=0
finally:
    f(t,n) if t.strip()=='' else f(n)