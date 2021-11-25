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

inp=Entry(win)
inp.pack()

def send():
    v=inp.get()
    print(v)
    color=choice(['red','green','blue'])
    win.configure(bg=color) 

btn=Button(win,text='Done',command=send)
btn.pack()







# botao = Button(win, text="Buscar cotações", command='pegar_cotacoes')
# botao.grid(column=0, row=1, padx=10, pady=10)

# texto_resposta = Label(win, text="")
# texto_resposta.grid(column=0, row=2, padx=10, pady=10)

win.mainloop()

