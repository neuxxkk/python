from python.pre import *
Clean.cls()
import requests as req
from bs4 import BeautifulSoup 
import matplotlib.pyplot as plt
from time import localtime as date
from tkinter import PhotoImage

soup = BeautifulSoup #Instanciando p/ ficar + fácil

day = date().tm_mday#                                            |
mon = date().tm_mon#  definindo como str para entar na URL  |
year = date().tm_year#                                      V

print(f'{mon}/{day}/{year}')

def graphic(period, coin):
  plt_days = [] # grafico com matplot
  plt_values = []

  #STYLE mtt chato
  plt.figure(num=f'{coin} Trading View', facecolor='#171B26')
  plt.axes(facecolor = '#171B26')
  plt.xticks(color = '#D1D4DC')
  plt.yticks(color = '#D1D4DC')
  sp = plt.subplot()
  sp.grid(color = '#2F3241')
  plt.subplots_adjust(left = 0.084, right = 0.95, bottom = 0.116, top = 0.895)
  plt.title(f'{coin}-BRL', font = 'candara', color = '#2962FF', fontsize = 15, fontweight = 'bold', loc='left', pad=17)
  plt.xlabel('Days', color = '#D1D4DC', labelpad=15, fontsize = 11)
  plt.ylabel('1BTC price', color = '#D1D4DC', labelpad=15, fontsize = 11)

#                            0 = início;  x = final(até);  -1 = steps(regressivo) 
  for i in range(period, 0, -1):
    y = str(year)
    m = str(mon).zfill(2)
    d = str(day-i).zfill(2)
    date = y+m+d
    url = f'https://economia.awesomeapi.com.br/xml/{coin}-BRL/?start_date=20230101&end_date={date}'

    btc = req.get(url)
    btc = soup(btc.text, 'xml') # formatando texto para xml(formato html)
    btc = float(btc.bid.text)
    plt_values.append(btc)
    plt_days.append(int(d))

  btc = soup(req.get(f'https://economia.awesomeapi.com.br/xml/last/{coin}-BRL').text, 'xml')
  btc = float(btc.bid.text)
  plt_values.append(btc)
  plt_days.append(day)

  t = plt.text(day-0.175, btc+0.05, str(btc), color = 'white', font = 'calibri', size = 11, fontstyle = 'normal', fontweight = 'bold')
  t.set_bbox(dict(facecolor = '#2962ff', boxstyle = 'round'))
  plt.plot(plt_days, plt_values, color = '#2962ff')
  plt.show()


graphic(3,'BTC')
