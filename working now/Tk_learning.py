from pre import *
Clean.cls()

import tkinter as tk

#initiating a window
window = tk.Tk() #--> The 'master'

#First setting
window.title('Tic-Tac-Toe')
window_frame = tk.Frame(master=window, width=150, height=150, bg='red')#Set the window as a frame (adding more functions to it, as, size, color ...)
window_frame.pack(fill=tk.Y,side=tk.LEFT)

r=tk.Frame(window, width=100,bg='#0f0')
r.pack(fill=tk.Y,side=tk.RIGHT)

#Program here
label1 = tk.Label(window, text = 'TicTacToe')#Creating a label (text box)
label1.pack()#place the indicated element


#keepping it in a loop so that dont close
window.mainloop()


#Discoverys
i = tk.Text(window, background='red')#Open a text box
i.place(x=0,y=0)