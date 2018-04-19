#print
#jedenfalls
#18-04-2018

#Dice Rolling Simulator
#140418
#jedenfalls

import random
#from random import randint

cal = ""
 
print("ENTER=Roll, Q=Quit")
 
while(cal != "Q"):
 i = random.randint(1, 6)

 print("\nroll?")
 cal = input()
 if(cal!="Q"): print(i)  
 else: print("no roll")