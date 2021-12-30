from pre import cls
cls()

r='User chose to not type anything'
def r_float(n):
    e='Digite um número real válido'
    while 1:
        try:x=float(input(n))
        except KeyboardInterrupt:
            print(f'\033[0;31mERROR: {r}\033[m')
            return 0
        except:print(f'\033[0;31mERROR: {e}\033[m')
        else:
            return x

def r_int(n):
    e='Digite um número inteiro válido'
    while 1:
        try:x=int(input(n))
        except KeyboardInterrupt:
            print(f'\033[0;31mERROR: {r}\033[m')
            return 0
        except:print(f'\033[0;31mERROR: {e}\033[m')
        else:
            return x
            


print(f'Integer typed: {r_int("Type an integer: ")}\nFloat typed: {r_float("Type a float: ")}')