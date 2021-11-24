from pygame import display, draw, time
from os import system
from pygame import event
from pygame.constants import QUIT

from pygame.event import wait
system('cls')

res=(720,720)
x=5
y=400

sur=display.set_mode(res)
sur.fill((0,190,30))

def line():
    draw.circle(sur,(255,0,0),(x,y),3,)

line()

i=0

for i in range(50):
    for ev in event.get():
        if ev.type==QUIT:quit()
    i=i+1
    x=x+2
    line()
    time.wait(50)
    display.flip()

i=0

for i in range(50):
    for ev in event.get():
        if ev.type==QUIT:quit()
    i=i+1
    y=y-2
    line()
    time.wait(50)
    display.flip()

i=0

for i in range(50):
    for ev in event.get():
        if ev.type==QUIT:quit()
    i=i+1
    x=x+2
    y=y+2
    line()
    time.wait(50)
    display.flip()

print('passo daq')

while 1:
    display.update()
    for ev in event.get():
        if ev.type==QUIT:quit()