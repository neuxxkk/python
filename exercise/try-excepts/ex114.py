from urllib import request
from pre import cls
cls()

try:site=request.urlopen('http://pudim.com.br')
except:e='Inacessível'
else:e='Acessível'
finally:print(f'Satus do site pudim.com: {e}')