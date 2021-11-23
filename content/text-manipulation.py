from pre import cls
cls()

frase=input('Type a frase: ')
x=input('Variables: ')

length=len(frase)
count=frase.count(x) #Conta quantas vezes 'x' aparece na frase
upper=frase.upper() #Transforma a frase em maiúscula
lower=frase.lower() #Transforma a frase em minúscula
capitalize=frase.capitalize() #Transforma o digito [0] da frase em caixa alta
title=frase.title() #Aplica o capitalize() em todas as palavras da frase
strip=frase.strip() #Elimina espaços antecedentes e sucessedente na frase - pode ser rstrip() && lstrip() - right and left
split=frase.split() #Transforma a frase em uma lista - cada palavra é um item
join=x.join(frase) #Adiciona 'x' a frase

print(f'The frase {join}')