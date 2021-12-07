from os import system
from sys import platform

system('pip install pygame')

if platform[0]=='l' or platform[0]=='d':
    def cls():
        system('clear')
elif platform[0]=='w':
    def cls():
        system('cls')
        
cls()
print('hello')