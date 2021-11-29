from os import system, times
from colorama.ansi import Fore
import webbrowser
system('cls')
import os

n=input('Wich past: ')

if n=='' or n[1]=='y':
    n='python'
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

webbrowser.open(f'https://github.com/neuxxkk/{n}')

from time import sleep

sleep(5)