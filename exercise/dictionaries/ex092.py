from datetime import datetime
from pre import cls
cls()

data=dict()
data['nome']=input('Nome: ')
data['nascimento']=int(input('Ano de nascimento: '))
data['ctps']=int(input('Ctps[0 n tem]: '))
data['idade']=datetime.now().year-data['nascimento']

if data['ctps']!=0:
    data['contratação']=int(input('Ano de contratação: '))
    data['sálario']=int(input('Salário: R$'))
    data['aposentadoria']=data['idade']+30
else:data['ctps']='Invalid'

print()
for k,v in data.items():
    print(f'Valor de {k.title()}: {v}') 
print()