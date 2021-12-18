from pre import cls
cls()

a=0
b=0
c=0
s=''

while 1:
    old=int(input('age: '))
    sex=input('gender: ')

    if sex.upper()[0]=='M':
        s='m'
    elif sex.upper()[0]=='F':
        s='f'

    if old>=18:a+=1

    if old<=20 and sex=='f':c+=1

    if s=='m':b+=1

    i=input('Again?: ')
    if i[0].lower()=='n':break

print(f'{a} pessoas são maiores de idade')
print(f'{b} pessoas são do sexo masculino')
print(f'{c} pessoas são mulheres com menos de 20 anos')