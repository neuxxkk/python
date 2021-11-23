from os import times
from pre import cls
from pygame import display, surface
import sys
from pygame.draw import polygon
from pygame import font
import pygame
cls()

res=(720,720)
cordinate=(250,250)

white=(255,255,255)
black=(255,255,255)

title='Move ball'
icon=pygame.image.load('m.png')
sur=pygame.display.set_mode(res)

sur.fill(white)
pygame.display.set_icon(icon)
pygame.display.set_caption(title)

pygame.display.init()
m=1
while m==1:
    for event in pygame.event.get():
        if event.type==pygame.QUIT: quit()


    texto='Hello, world!'

    pygame.font.init()

    fonte='candara'

    f=pygame.font.SysFont(fonte,35)

    txt = f.render(texto, 1, (0,0,0))

    sur.blit(txt,(50,100))
    pygame.display.update()

    # pygame.draw.circle(sur,black,(250,250),25)

    # display.update()
    # pygame.time.delay(1000)
    # pygame.draw.line(sur,black,(0,250),(250,250))
    
    
    # pygame.time.delay(5000)
