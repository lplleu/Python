#jedenfalls
#29-04-2018
#hanoi, yet, yet again 

def hanoi(n,source,spare,destination):
  if n > 0: #
    hanoi(n-1,source,destination,spare) # move everything but the bottom disc to spare spindle via destination
    print("move disc",n,"from",source,"to",destination) #
    hanoi(n-1,spare,source,destination) #reset; move remaining stack from spare to destination via source
          
          #my source is the spindle b, my spare is the sprindle a, and my destination is spindle c
          
          
if __name__ == "builtins":
  hanoi(3,"a","b","c")
  
  #beautiful (1420)
