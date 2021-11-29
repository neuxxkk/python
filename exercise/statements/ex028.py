from math import nan
from colorama.ansi import Fore
import pygame
from pre import cls
from pygame import *
import colorama
from random import randint
cls()

white=Fore.WHITE
red=Fore.RED
green=Fore.GREEN
pink=Fore.MAGENTA

def st(x):
    print(red,'-=-'*25,green)
    if x:
        print(white)

st(False)
print('         I will think in a number between 0 and 5. Try guess...')
st(True)

n=randint(0,5)
x=int(input('What is the number? '))
c=0
cor=''

print(pink,'\nProcessing...\n',white)
time.delay(1500)

if x==n:
   c='RIGHT'
   cor=green
else:
    c='WRONG'
    cor=red

print(f'Number = {n}\n\nYou are {cor}{c}{white}\n')

