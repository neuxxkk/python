from os import truncate
from pre import cls
cls()

import pygame
pygame.init()
n=pygame.mixer.music.load('hi.mp3')
pygame.mixer.music.play()
pygame.time.delay(100000)
#while True:
    #print('ola')
    #pygame.time.delay(1000)
    #print('tchau')
    #pygame.time.delay(1000)