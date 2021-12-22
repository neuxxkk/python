from pre import cls
cls()

op=0
cl=0
n=input('expressão: ')
for i in n:
    if i=='(':op+=1
    elif i==')':cl+=1

print('\nok!\n') if op==cl else print('\nfail\n')