from os import system
system('cls')
import requests
from bs4 import BeautifulSoup

url='https://instagram.com'
req=requests.get(url)
txt=req.text

soup=BeautifulSoup(txt, 'html.parser')
soup.prettify()
print(soup.title)

# print(txt.title)



# from googlesearch import search
# for url in search("instagram", lang="en",stop=10):
#     print(url)

# for url in search(ip, stop=20):
#      print(url)


