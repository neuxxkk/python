import time
import datetime
from pre import cls
cls()

y=time.localtime().tm_year
for i in range(7):
    n=int(input(f'bd year{i+1}: '))
    if y-n>=18:
        print('legal age') 
    else:print('not legal age')