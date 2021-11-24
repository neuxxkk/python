import os
from pygame import *
import time
from os import system

from pygame.time import wait
system('cls')

conf=False

alarm_hour=int(input('alarm hour: '))
alarm_minute=int(input('alarm minute: '))
alarm_tempo=(alarm_hour,alarm_minute)

x=time.localtime()
hour=x.tm_hour
minute=x.tm_min
tempo=(hour,minute)
print(f'{hour}:{minute}')

def count():
    x=time.localtime()
    hour=x.tm_hour
    minute=x.tm_min
    tempo=(hour,minute)
    # print(f'{hour}:{minute}')

res=(720,720)
black=(0,0,0)
green=(0,200,0)

def config_pygame():
    x=time.localtime()
    hour=x.tm_hour
    minute=x.tm_min
    tempo=(hour,minute)

    scrn=display.set_mode(res)
    scrn.fill(black)
    font.init()
    t=font.SysFont('candara',60,bold=True)
    t1=font.SysFont('calibri',60,bold=True)
    txt=t.render('Jogo do Galo!',True,(255,255,255))
    txt1=t1.render(f'{hour}:{minute}',True,(255,255,255))
    scrn.blit(txt,(200,260))
    scrn.blit(txt1,(300,350))

def alarm():
    print(f'{hour}:{minute}')
    config_pygame()
    print('Hora do jogo!')
    while 1:
        display.update()
        for ev in event.get():
            if ev.type==KEYDOWN:
                if ev.key==K_m:
                    quit()
                    wait(300000)
                    alarm()
                if ev.key==K_SPACE:
                    quit()
            if ev.type==QUIT:quit()

def condition(suspend):
    wait(suspend)
    if tempo==(alarm_tempo):
        alarm()
        conf=True

while not conf:
    x=time.localtime()
    hour=x.tm_hour
    minute=x.tm_min
    tempo=(hour,minute)
    condition(0)
    print(tempo)

    
