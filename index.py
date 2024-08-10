"""A classic casino slot machine playable in the terminal"""


import random


def spin():
 playerList = []
 for i in range(3):
  playerChoice= random.randint(2,4)
  playerList.append(playerChoice)

 return playerList



def playGame():
 val = input("Do you want to play? (Y/N) ")

 if val =="Y":
  balance = input("How much do you want to deposit? ")
  start = input("Start game? (Y/N) ")
  if start =="Y":
     balance = int(balance)-10
     print(f"you have ${balance} remaining")
  if all(ele ==2 or ele ==3 for ele in spin()):
   balance = int(balance)+10
   print(f"You Win! Your balance is now ${balance}")
   while balance > 0:
    choice= input("spin again?(Y/N) ")
    if choice == "Y":
     if all(ele ==2 or ele ==3 for ele in spin()):
      balance=int(balance)+10
      print(f"You Win! Your balance is now ${balance}")
     elif all(ele ==1 for ele in spin()):
      balance = int(balance)+100
      print(f"You hit the JACKPOT!")
     else:
      balance=int(balance)-10
      print(f"You Lose! Your balance is now ${balance}")
    else:
     print(f"Game Over. Your remaining balance is {balance}") 
     return
   if balance<=0:
      print(f"Game Over. Your remaining balance is {balance}")
      playGame()
  elif all(ele ==1 for ele in spin()):
   balance = int(balance)+100
   print(f"You hit the JACKPOT!")    
  else:
   print(f"You Lose! Your balance is now ${balance}")
   while balance > 0:
    choice= input("spin again?(Y/N) ")
    if choice == "Y":
     if all(ele ==2 or ele ==3 for ele in spin()):
      balance=int(balance)+10
      print(f"You Win! Your balance is now ${balance}")
     elif all(ele ==1 for ele in spin()):
      balance = int(balance)+100
      print(f"You hit the JACKPOT!")
     else:
      balance=int(balance)-10
      print(f"You Lose! Your balance is now ${balance}")
    else:
     print(f"Game Over. Your remaining balance is {balance}") 
     return
   if balance<=0:
      print(f"Game Over. Your remaining balance is {balance}")
      playGame()

 elif val =="N":
  return
 else:
  print("Invalid Response")
  playGame()




playGame()