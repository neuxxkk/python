from os import system
import sys
from pygame import event, key

from pygame.constants import K_0, K_DOWN, K_LEFT, K_RIGHT, K_SPACE, K_UP, KEYDOWN, KEYUP
system('cls')
import pygame
import pygames

w=720
h=720
res=(w,h)
black=(0,0,0)
white=(255,255,255)
x=0
y=0
cor=(x,y)


screen=pygame.display.set_mode(res)
ball=pygame.image.load('m.png')
gol1=pygame.image.load('gol1.png')
gol2=pygame.image.load('gol2.png')
pygame.display.set_caption('Role ball')
pygame.display.set_icon(ball)

screen.fill((255,0,0))
screen.blit(ball,cor)
screen.blit(gol1,(300,0))
screen.blit(gol2,(300,600))


sawa=1
while True:
    pygame.init()
    pygame.display.init()
    for ev in pygame.event.get():
        if ev.type==KEYDOWN:
            if ev.key==K_RIGHT:
                t=0
                for t in range(30):
                    t=t+1
                    x=x+3
                    screen.fill((255,0,0))
                    screen.blit(gol1,(300,0))
                    screen.blit(gol2,(300,600))
                    cor=(x,y)
                    print(cor)
                    screen.blit(ball,cor)
                    pygame.display.flip()
                    pygame.event.wait(50)
            elif ev.key==K_DOWN:
                t=0
                for t in range(30):
                    t=t+1
                    y=y+3
                    screen.fill((255,0,0))
                    screen.blit(gol1,(300,0))
                    screen.blit(gol2,(300,600))
                    cor=(x,y)
                    print(cor)
                    screen.blit(ball,cor)
                    pygame.display.flip()
                    pygame.event.wait(50)
            elif ev.key==K_LEFT:
                print('left')
                t=0
                for t in range(30):
                    t=t+1
                    x=x-3
                    screen.fill((255,0,0))
                    screen.blit(gol1,(300,0))
                    screen.blit(gol2,(300,600))
                    cor=(x,y)
                    print(cor)
                    screen.blit(ball,cor)
                    pygame.display.flip()
                    pygame.event.wait(50)
            elif ev.key==K_UP:
                print('up')
                t=0
                for t in range(30):
                    t=t+1
                    y=y-3
                    screen.fill((255,0,0))
                    screen.blit(gol1,(300,0))
                    screen.blit(gol2,(300,600))
                    cor=(x,y)
                    print(cor)
                    screen.blit(ball,cor)
                    pygame.display.flip()
                    pygame.event.wait(50)

        if y>500 or y<90:
            fonte=pygame.font.SysFont('candara',40)
            f=fonte.render('gool',1,(0,0,0))
            screen.blit(f,(300,300)) 
            pygame.display.update()
            pygame.time.delay(1000)
            screen.fill((255,0,0))
            screen.blit(gol1,(300,0))
            screen.blit(gol2,(300,600))
            x=300
            y=300
            cor=(x,y)
            screen.blit(ball,cor)           



                # for i in range(4):
                #     screen.fill((255,0,0))
                #     print(i)
                #     x=x-10
                #     cor=(x,y)
                #     pygame.time.delay(200)
                #     screen.blit(ball,cor)
        
        if ev.type == pygame.QUIT: pygame.quit()

    pygame.display.update()
