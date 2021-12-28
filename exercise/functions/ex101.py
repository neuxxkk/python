from datetime import datetime
from pre import cls
cls()

def f(x):
    a=datetime.now().year-x
    if a<16:c='PROIBIDO' 
    elif a<18 or a>60:c='OPCIONAL'
    else: c='OBRIGATÓRIO'
    return(f'Voto com {a} anos = {c}')

print(f(int(input('Data de nascimento: '))))
