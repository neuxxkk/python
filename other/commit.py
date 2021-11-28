from os import system
from colorama.ansi import Fore
system('cls')
import os

n=input('Wich past: ')

if n[1]=='y' or n=='':
    path='C:/Users/32165/Desktop/code/python'
else:
    print(Fore.RED,'Must be on Desktop!',Fore.WHITE)
    path=f'C:/Users/32165/Desktop/{n}'

    

os.chdir(path)
print(os.getcwd())
def git(x):
    system(f'git {x}')

git('status')
git('add .')
git('commit -m "a"')
git('push')