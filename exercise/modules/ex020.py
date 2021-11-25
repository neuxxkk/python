from math import log, log2
import pre
pre.cls()
import random

x=[]
n=0
r=[]
y=''

def add():
  global n
  global y
  n+=1
  a=input('Type a name: ')
  x.append(a)

for i in range(4):
  add()

y=input('Another name? Y/N ')

while y=='Y'or y=='y':
  add()
  y=input('Another name? Y/N ')
else:
  def sort():
    log(n)
    global r
    r=random.sample(x,k=n)

  def imp():
    for i in range(n):
      i+=1
      print(f'{i}º escolhido foi: {r[i-1]}')

sort()
imp()


