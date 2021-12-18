from pre import cls
cls()

i=0
min=0
max=0
total=0
caro=0
while 1:
    i+=1
    print(f'\nProduct {i}\n')
    name=input('name: ')
    price=float(input('price: R$'))

    if i==1:
        min=price
    else:
        if price<min:min=f'{name} : R${price}'

    if price>1000:
        caro+=1

    total+=price

    x=input('Again?: ')
    if x.upper()[0]=='N':break

print(f'\nTotal: R${total:.2f}')
print(f'Produtos acima de 1k: {caro}')
print(f'Produto mais barato: R${min:.2f}')