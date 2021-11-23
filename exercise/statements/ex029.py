from typing import Text
from pygame import display, surface
import sys

from pygame.draw import polygon
from pre import cls
cls()

import pygame

c=(0,255,255)
c2=(255,0,0)

x='oi'
i=pygame.image.load('m.jpg')

sur=pygame.display.set_mode(size=(500,500))
sur.fill(c)
pygame.display.set_icon(i)
pygame.display.set_caption('Hello')

pygame.display.init()


pygame.font.init()
f=pygame.font.SysFont('Candara',35)
txt=f.render('hello',True,c2)

sur.ren
# pygame.draw.circle(sur,c2,(250,250),25)

display.update()
# pygame.time.delay(1000)
# pygame.draw.line(sur,c2,(0,250),(250,250))
# sur.blit(txt,(250,250,100,50),(500,500,200,100))
print(txt)
pygame.display.update()
pygame.time.delay(5000)

