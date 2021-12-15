from os import system
from time import sleep
system('clear')

red='\033[1;31m'
green='\033[1;32m'
orange='\033[1;33m'
blue='\033[1;34m'
purple='\033[1;35m'

print(f'{"-=-"*3}{red}ANSI {green}COLOR {purple}CODE{"-=-"*3}')

print(f'\n\033[1;30m{"-"*5}STYLE{"-"*5}')
for i in range(5):
    print(f'\033[0;0;0m\033[{i}mHello, world! - [{i};0;0m')
    sleep(0.2)

sleep(0.5)
    


print(f'\n\033[1;31m{"-"*5}COLOR{"-"*5}')
for i in range(8):  
    print(f'\033[0;0;0m\033[0;{i+30}mHello, world! - [0;{i+30};0m') 
    sleep(0.2)    

sleep(0.5)

print(f'\n\033[1;32m{"-"*5}BGCOLOR{"-"*5}')
for i in range(8):
    print(f'\033[0;0;0m\033[37;{i+40}mHello, world! - [0;0;{i+40}m')
    sleep(0.2)

sleep(0.5)

print('\033[0m')