from pre import cls
cls()

def app():
  n1=int(input('number 1: '))
  n2=int(input('number 2: '))

  
  print('[1] soma')
  print('[2] subtracao')
  print('[3] multiplicacao')
  print('[4] divisao')
  print('[5] novos numeros')
  print('[6] sair do app')
  
  t=int(input('\n'))
  
  if t== 1:print(f'{n1}+{n2}={n1+n2}')
  if t== 2:print(f'{n1}-{n2}={n1-n2}')
  if t== 3:print(f'{n1}x{n2}={n1*n2}')
  if t== 4:print(f'{n1}/{n2}={n1/n2}')
  if t== 5:app()
  if t== 6:q=1

app()
while q== 0: 
  app()