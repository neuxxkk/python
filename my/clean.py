import os
import platform
p=platform.platform()


u=input('pc-user: ')

if p[0].lower()=='l':
    os.system('clear')
    h=f'/home/{u}/Desktop'
    d='rm -r'
else:
    h=f'C:/Users/{u}/Desktop'
    d='del'

def find(x):
    n=f'{h}/python/{x}'
    os.chdir(n)
    e=f'{n}/__pycache__'
    if os.path.exists(e):
        os.system(f'{d} __pycache__') 
        os.system('rmdir __pycache__')
    os.system('dir')

find('')

find('exercise/modules')
find('exercise/statements')
find('exercise/loops-for')
find('exercise/loops-while')
find('exercise/tuples')
find('exercise/lists')
find('exercise/')

find('my')

find('other')

find('content')
find('content/os')
find('content/pygame')

find('')

