from pre import cls
cls()

n=(
    ('leite  ','R$  3,00 '),
    ('maçã   ','R$  2,00 '),
    ('cereal ','R$  5,00 '),
    ('perfume','R$ 15,00 '),
    ('iogurte','R$  7,00 ')
)

print(f'  | Produtos{" "*2}|{" "*2}Preço    |')
print(f'  ------------------------')
for i in range(len(n)):
    f=f'{" "*2}|{" "*2}'.join(n[i])
    print(f'  |  {f}|')
print(f'  ------------------------')


