from math import nan
from colorama.ansi import Fore
import pygame
from pre import cls
from pygame import *
import colorama
import time
from random import randint
cls()

white=Fore.WHITE
red=Fore.RED
green=Fore.GREEN
pink=Fore.MAGENTA

def all():
    def st(x):
        print(red,'-=-'*25,green)
        if x:
            print(white)

    st(False)
    print('         I will think in a number between 0 and 10. Try guess...')
    st(True)

    n=randint(0,10)
    x=int(input('What is the number? '))
    c=0
    cor=''

    print(pink,'\nProcessing...\n',white)
    time.sleep(1.5)

    global f
    if x==n:
        f=1
        c='RIGHT'
        cor=green
    else:
        f=0
        c='WRONG'
        cor=red

    print(f'Number = {n}\n\nYou are {cor}{c}{white}\n')
    time.sleep(1.5)

all()
while f==0:cls(),all()
