#Guess the number
#140418
#jedenfalls

import random

i = random.randint(1,6)
ans = ""
guess = 1

if(guess==""):
  guess = int(input("no value, Guess the integer between 1 and 6"))
#elif(eval(guess)==""):
#  guess = input("no value, Guess the integer between 1 and 6")
else:
  guess = int(guess)
  tries = 1
  
  while(guess<1): 
    print("out of range. min = 1")
    guess = int(input("\nGuess the integer between 1 and 6\n"))

  guess = int(input("Guess the integer between 1 and 6.\n"))
    
  while(guess!="N"):
    while(guess!=i):
     if(guess=="N"):
       print("you chose to leave the game")
     elif(int(guess)>6): 
       print("out of range, max = 6")
       guess = int(input("\nGuess the integer between 1 and 6\n"))
     elif(int(guess)<i):
       print("nope, go higher")
       tries+=1
       guess = int(input(""))
     else:
       print("nope, go lower")
       tries+=1
       guess = int(input(""))

    if(tries==1):
      print("genau!,first try!!!!")
    else:
      print("yeah,",tries,"tries")
  
    guess = input("\ntry again? press N to quit.\n")
    tries = 1
    i = random.randint(1, 6)