#jedenfalls
#hanoi, yet again
#29-04-2018

#divide and conquer

#step 1; move n-1 stack to spare via destination
#step 2; move remaining disc from source to destination
#step 3; move n-1 stack to destination via source

def hanoi(n,source,spare,destination):
  if n>0:
    hanoi(n-1,source,destination,spare) ###oooh... remember the positiono of the SPARE as per syntax!!!
    print("move disc",n,"from",source,"to",destination)
    hanoi(n-1,spare,source,destination)
  
if __name__=="builtins":
  hanoi(3,"a","b","c")
  
  
#eish, this is not easy. 1345
