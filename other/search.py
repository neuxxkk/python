from os import system
import pygame
system('cls')
import requests
from bs4 import BeautifulSoup
from pygame import time

ask=input('Name of the site: ')
url=f'https://{ask}.com'
req=requests.get(url)
txt=req.text

soup=BeautifulSoup(txt, 'html.parser')
soup.prettify()
print(soup.title)
time.wait(2000)

# print(txt.title)



# from googlesearch import search
# for url in search("instagram", lang="en",stop=10):
#     print(url)

# for url in search(ip, stop=20):
#      print(url)


