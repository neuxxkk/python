from pre import cls
cls()

n_u=input('frase: ')
n_u1=n_u.replace(' ','')
n_p=n_u1[::-1]

print(f'"{n_u}" é um palíndromo') if n_p==n_u1 else print(f'"{n_u}" não é um palíndromo')
    
