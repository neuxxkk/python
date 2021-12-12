from pre import cls
cls()

peso=float(input('peso em kg: '))
altura=float(input('altura em m: '))
imc=peso/(altura**2)

print(f'IMC = {imc:.2f}')

if imc<18.5:status='abaixo do peso'
elif imc<25:status='peso ideal'
elif imc<30:status='sobrepeso'
elif imc<40:status='obesidade'
else:status='obesidade mórbida'

print(status)
