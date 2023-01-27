from os import system
from sys import platform

class Clean():
    if platform[0]=='l' or platform[0]=='d':
        def cls():
            system('clear')
    elif platform[0]=='w':
        def cls():
            system('cls')
            
    cls()
    print('hello')

class Colors():
    q = '\033['

    #style
    default = f'{q}0m'
    bold = f'{q}1m'
    bright = f'{q}2m'
    italic = f'{q}3m'
    underl = f'{q}4m'

    #color
    black_font = f'{q}30m'
    red_font = f'{q}31m'
    green_font = f'{q}32m'
    yellow_font = f'{q}33m'
    blue_font = f'{q}34m'
    purple_font = f'{q}35m'
    light_blue_font = f'{q}36m'
    white_font = f'{q}37m'

    #bg_color
    black_bg = f'{q}40m'
    red_bg = f'{q}41m'
    green_bg = f'{q}42m'
    yellow_bg = f'{q}43m'
    blue_bg = f'{q}44m'
    purple_bg = f'{q}45m'
    light_blue_bg = f'{q}46m'
    white_bg = f'{q}47m'
