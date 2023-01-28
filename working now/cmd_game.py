#LIBS
from python.pre import *
import random
import time
import emoji
import string

#
Clean.cls()
q = '\033['
slp = time.sleep
user_points = 0 
pc_points = 0
global solved


#Config
class Init():

  def menu():
    Clean.cls()
    print(f'{Colors.bold}\t\t\t{Colors.red_font}G{Colors.green_font}A{Colors.yellow_font}M{Colors.blue_font}E{Colors.purple_font}S{q}0m')
    print(f'Pc points: {pc_points}\t\t\t\t\tUser points: {user_points}')
    print(f'\n{q}2;0m1 - {q}0;35mGuess the Number\n\n{q}2;0m2 - {q}0;34mJokenpo\n\n{q}2;0m3 - {q}0;33mPassword Generator\n\n{q}2;0m4 - {q}0;32mTic-tac-toe\n\n{q}2;0m5 - {q}0;31mHangman{Colors.default}\n\n6 - Quit->\n')
    global game_number
    game_number = int(input(': '))
    Error.Out_of_range(Init.menu, game_number, 1, 6)
    Init.run()

  def run():
    Clean.cls()
    if game_number == 1:Game.Guess.guess_number()
    if game_number == 2:Game.Jokenpo.jok()
    if game_number == 3:Game.PwdGen.pwd()
    # if game_number == 4:Game.Guess.guess_number()
    # if game_number == 5:Game.Guess.guess_number()
    if game_number == 6:quit()
  
  def back(x,z='Try'):
    decision = int(input(f'\n\n\n1. Back to menu < \t\t\t\t\t\t\t\t\t\t 2. {z} again <\n\n:'))
    Error.Out_of_range(Init.back, decision, 1, 2)
    Clean.cls()
    Init.menu() if decision == 1 else x()

#General
class Game():

  def decoration(font,bg):
    input(f'{font}{"-="*20}{bg}WELCOME TO THE GUESS GAME{Colors.default}{font}{"-="*20}{Colors.default}\n\n\t\t\t\t\tpress enter to start')
  global decor
  decor = decoration

  class Guess():
    #Init Guess
    def guess_number():
      print("1. Guess PC's number\n2. Let PC guess your number")
      choice = int(input('\n'))
      Error.Out_of_range(Game.Guess.guess_number, choice, 1, 2)
      Clean.cls()
      if choice == 1: Game.Guess.gn1()
      elif choice == 2: Game.Guess.gn2()

    #User guessing
    def gn1():
      #Decoration
      decor(Colors.yellow_font,Colors.purple_bg)

      Clean.cls()

      print('\t\t\t\t\t\n\n\n',end='')
      for i in "Ok I'm going to think in a number...":
        slp(0.1)
        print(i, end='', flush=1)
      slp(1)

      Clean.cls()

      print('\t\t\t\t\t\n\n\n',end='')
      print('My number is bettwen 0 and 10\n')
      slp(1.1)
      
      #Generating randint
      number = random.randint(0,10)

      while 1:
        user_guess = int(input('Your Guess: '))
        if user_guess < 0 or user_guess > 10:
          Error.mesage('Number out of range', 1.5)
        else: break
      if 0:
      # while user_guess != number:
      #   print('To low try again!') if user_guess < number else 'too high try again!'    -->> Repeat until won (sucks)
      #   user_guess = int(input())
      #   print('Congrats! You got it right!')
        0   
      Clean.cls()

      #Decoration
      for i in range(9):
        slp(0.2)
        print('.', end='', flush=1)
        if (i+1)%3==0:
          slp(0.3)
          Clean.cls()

      print(f'\t\t\t\t{Colors.blue_font}THE NUMBER IS {q}1;33m{number}{Colors.default}\n\n')

      #Checking
      if number == user_guess:
        print(f'\t\t\t\t{Colors.bold}{Colors.green_font}YOU ARE RIGHT!{Colors.default}')
        global user_points
        user_points += 1
      else:
        print(f'\t\t\t\t{Colors.bold}{Colors.red_font}YOU ARE wrong!{Colors.default}')
      
      Init.back(Game.Guess.gn1)
         
    #Pc Guessing
    def gn2():
      decor(Colors.purple_font,Colors.yellow_bg)

      Clean.cls()

      for i in 'Ok now i have to guess your number':
        slp(0.1)
        print(i,end='',flush=1)

      slp(1)

      Clean.cls()

      print('\nCould you give me a range? (=\n\n')
      slp(0.2)

      while 1:
        max = int(input('Max: '))
        min = int(input('Min: '))
        if max <= min:
          Error.mesage('MAXIMUM must be bigger than MINIMUM', 2)
        else: break

      pc_guess = random.randint(min,max)

      Clean.cls()
      f = 'I think it is...'
      for i in f:
        print(i,end='',flush=1)
        slp(0.15)

      Clean.cls()
      print('I think it is',end='',flush=1)
      for x in range(6):
        slp(0.15)
        print('.',flush=1,end='')
        slp(0.15)
        if (x+1)%3 == 0:
          Clean.cls()
          print('I think it is',end='',flush=1)
      
      print(f':\t{q}1;35m{pc_guess}{Colors.default}')

      print(f'\n\t\t{q}3mAm i right?\n\n{q}1;32m1.YES\t\t\t\t\t{Colors.red_font}2.NO{Colors.default}')
      result = int(input())

      if result == 1:
        print(f'\n\n\t\t{q}1;32mUHULL!!! I knew it! (~;{Colors.default}')
        global pc_points
        pc_points += 1
      else:
        print(f'\n\n\t\t{q}1;31mAhhhh! )~:{Colors.default}')

      Init.back(Game.Guess.gn2)
        
  class Jokenpo():
    def jok(): 

      options = {
        'r' : emoji.emojize(':fist:', language = 'alias'),
        'p' : emoji.emojize(':raised_hand:', language = 'alias'),
        's' : emoji.emojize(':v:', language = 'alias')
      }

      #Choices & decorations 
      decor(Colors.blue_font,Colors.green_bg)

      Clean.cls()
      pc_choice = random.choice(['r', 'p', 's'])

      while 1:
        user_choice = input(emoji.emojize("I've chosen mine and you?\n\nR. :fist:\t\tP. :raised_hand:\t\tS. :v:\n\n:", language='alias')).lower()
        if user_choice not in 'rps':Error.mesage(f'"{user_choice}" is not an option: r,p,s', 2) 
        else:break

      global pc_points,user_points

      if pc_choice != user_choice:
         if pc_choice == 'r' and user_choice == 's' or 'p' and 'r' or 's' and 'p':
          pc_points += 1
          msg = f'{q}1;32mI won!! UHULL! {Colors.purple_font}(={Colors.default}'
         else: 
          user_points += 1
          msg = f'{q}1;32mYou won! {Colors.red_font}Ahhh ):{Colors.default}'
      else:
        user_points += 1
        pc_points += 1
        msg = f'{q}2mDraw \={Colors.default}'

      user_choice = options[user_choice]
      pc_choice = options[pc_choice]

      Clean.cls()

      for i in range(9):
        slp(0.2)
        print('.', end='', flush=1)
        if (i+1)%3==0:
          slp(0.3)
          Clean.cls()

      print(f'\t\t\t\t\t\tYou> {user_choice} x {pc_choice}  <Me\n\n\n\t\t\t\t\t{msg}')

      Init.back(Game.Jokenpo.jok)
      
  class PwdGen():
    def pwd():
      
      decor(Colors.red_font,Colors.green_bg)

      Clean.cls()

      qtd = int(input('How many passwords? '))
      size = int(input('How long? '))

      print('\nHere it is your passwords:')

      for i in range(qtd):
        print(f'\n{i+1}. ', end='')
        pwd = ''
        for c in range(size):
          r = random.randint(0, 93)
          d = string.printable[r]
          pwd += d
          print(d,end='',flush=1)
          slp(0.1)
      

      Init.back(Game.PwdGen.pwd, z = 'Go')
      

  class TicTacToe():
    0

  class Hangman():
    0

#Errors
class Error():

  def mesage(msg, time):
    Clean.cls()
    print(f'{Colors.red_font}ERROR: {msg}{Colors.default}')
    slp(time)
    Clean.cls()

  def Out_of_range(function, var, min, max):
    if var < min or var > max: 
      Error.mesage('This number is out of range', 1.5)
      function()

#Starting game  
Init.menu()  
