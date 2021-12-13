from pre import cls
cls()

maior=0
menor=0
for i in range(5):
    peso=float(input(f'peso{i+1}: '))
    if i==1:
        maior=peso
        menor=peso
    else:
        if peso>maior:
            maior=peso
        if peso<menor:
            menor=peso

print(f'\nmaior: {maior}')
print(f'menor: {menor}')