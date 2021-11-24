import os
from pygame import *
import pygame
import time
from os import system
from pygame.display import update

from pygame.time import wait
system('cls')

res=(720,720)
black=(0,0,0)
green=(0,200,0)
conf=False

def start():
    pygame.init()
    ico=image.load('icon.png')
    alarm_img=image.load('alarm.png')
    display.set_icon(ico)
    display.set_caption('Alarm')
    scrn=display.set_mode(res)
    scrn.fill(black)
    font.init()
    t=font.SysFont('candara',60,bold=True)

    scrn.fill((60,200,90))
    txt_start=t.render('Alarm',True,(255,69,0))
    scrn.blit(txt_start,(265,280))
    scrn.blit(alarm_img,(310,370))
    display.update()

start()

while 1:
    
    display.update()
    for ev in event.get():
        if ev.type==QUIT or ev.type==KEYDOWN:
            quit()
            alarm_hour=int(input('Alarm hour: '))
            alarm_minute=int(input('Alarm minute: '))
            alarm_tempo=(alarm_hour,alarm_minute)
            message=input('Message: ')

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

                scrn.fill(black)

                txt=t.render(message,True,(255,255,255))
                txt1=t1.render(f'{hour}:{minute}',True,(255,255,255))
                scrn.blit(txt,(200,260))
                scrn.blit(txt1,(300,350))



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




            def alarm():
                print(f'{hour}:{minute}')
                config_pygame()
                print(message)
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
                system('cls')
                x=time.localtime()
                hour=x.tm_hour
                minute=x.tm_min
                tempo=(hour,minute)
                condition(0)
                print(tempo)
                wait(10)

                

