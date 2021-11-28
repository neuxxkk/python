from pygame.constants import QUIT
from pre import cls
cls()

import pygame

import random

i=1
n=[]

while 1:
    for i in range(4):
        x=input(f'Nome{i}: ')
        n.append(x)

    i=random.randint(1,4)

    print(f'O sorteado foi {n[i]}')
    if pygame.event == QUIT:
        quit()