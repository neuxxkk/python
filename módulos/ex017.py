from pre import cls
cls()

import math
co=float(input(f'Comprimento do cateto oposto: '))
ca=float(input(f'Comprimento do cateto adjacente: '))

n=math.hypot(co,ca) # Igual a: x=(co**2)+(ca**2) x**(1/2)
print(f'A hipotenusa dos catetos: {co} e {ca} é {n:.2f}')