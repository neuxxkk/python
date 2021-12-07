from pre import cls 
cls()
import os

os.system('pip install pydirectory')

import pydirectory



def find(x):
    n=f'C:/Users/32165/Desktop/code/python/{x}'
    os.chdir(n)
    e=f'{n}/__pycache__'
    if os.path.exists(e):
        os.system('del __pycache__') 
        os.system('rmdir __pycache__')
    os.system('dir')

find('')

find('exercise/modules')
find('exercise/statements')
find('exercise')

find('my')

find('other')

find('content')
find('content/os')
find('content/pygame')

find('')

