from math import nan

import pygame
from pre import cls

from pygame import *
from random import randint
cls()

n=randint(0,5)
x=int(input('Guess a number: (0:5) '))
c=0

print('Processing...')
time.delay(1500)

if x==n:
   c='right' 
else:
    c='wrong'

print(f'Number={n}\nYou are {c}')

