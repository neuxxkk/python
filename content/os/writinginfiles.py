from os import *
import time
import os, signal

os.system('cls')

dir='C:/Users/32165/Desktop'

# os.startfile('C:/Users/32165/Desktop/teteu.png')
x=os.open('C:/Users/32165/Desktop/kill.txt',O_RDWR|O_CREAT)
t='Hello, world!'
txt=t.encode()
os.write(x,txt)

os.close(x)

p=os.startfile(f'{dir}/kill.txt')

pid=os.getpid()

time.sleep(2)

os.remove(f'{dir}/kill.txt')


# print(x)