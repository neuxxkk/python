from random import choice
from os import system
from types import coroutine
from typing import Collection
system('cls')
from tkinter import *
import tkinter

win = Tk()
win.geometry('300x150')
win.title("Hello")


t='Hello, world'
txt=Label(win,text=t) 
txt.pack()

inp=Entry(win)#input text
inp.pack()

def send():
    v=inp.get()#get the input text
    print(v)
    color=choice(['red','green','blue'])
    win.configure(bg=color)#master configs such as color

btn=Button(win,text='Done',command=send)
btn.pack()

win.mainloop()

