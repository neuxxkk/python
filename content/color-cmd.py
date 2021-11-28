from pre import  cls
cls()
from colorama import Fore,Back,Style
from pygame import *

print(f'{Fore.GREEN}{Back.YELLOW}{Style.BRIGHT}Hello, world!')

while 1:
    time.wait(1)
    
    init()
    for ev in event.get(): 
        if ev.type==QUIT:
            quit()