import os

def update_repo(repo_path: str, commit_message: str):
    os.chdir(repo_path)
    os.system('git add .')
    os.system(f'git commit -m "{commit_message}"')
    os.system('git pull')
    os.system('git push')
    print("Repositório atualizado com sucesso!")

def main():
    repo_path = input("Digite o caminho para o repositório: ")
    commit_message = input("Digite a mensagem de commit: ")
    if os.path.exists(repo_path):
        update_repo(repo_path, commit_message)
    else:
        print("Caminho do repositório inválido.")

if __name__ == "__main__":
    main()

# from os import system, times
# # system('pip install colorama')
# # from colorama.ansi import Fore
# import webbrowser
# import os
# import platform



# p=platform.platform()
# u=os.getlogin()

# if p[0].lower()=='l':
#     system('clear')
#     h=f'/home/{u}/Desktop'
# else:
#     system('cls')
#     h=f'C:/Users/{u}/Desktop'

# print('Must be on Desktop!')

# n=input('Wich past: ')

# if n=='' or n[1]=='y':
#     n='python'
#     path=f'{h}/python'
# else:
#     path=f'{h}/Desktop/{n}'
    

# os.chdir(path)
# print(os.getcwd())
# def git(x):
#     system(f'git {x}')
    
    
# git('status')
# git('add .')
# git('commit -m "a"')
# git('push')

# webbrowser.open(f'https://github.com/neuxxkk/{n}')

# from time import sleep

# sleep(5)
