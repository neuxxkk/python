import os
os.system('cls')

app_path='chrome'

os.system(f'start {app_path}') # Comando no cmd
 
#  || OR ||

dir='C:/Program Files' # Pasta com files.exe -mais correto

os.startfile(f'{dir}/Google/Chrome/Application/chrome')

#  || OR ||

dir1='C:\ProgramData\Microsoft\Windows\Start Menu\Programs' # Pasta com Atalhos do Menu Start -mais fácil de localizar

os.startfile(f'{dir1}/Google Chrome')

