#what this really means is, "move the stack n-1 from a to b; using c as a spare"

def hanoi(n,source,spare,destination):
  #stopping case
  if n>0: #there is nothing to solve if n==0
    hanoi(n-1,source,destination,spare) #290418 -what is the purpose of "spare" here??????
    #ans to above, the function takes 3 parameters, which are then later rearranged
    print("move disk",n,"from",source,"to",destination)
    hanoi(n-1,spare,source,destination)  # I think this is the key. this is the +reset+. then rinse and repeat.

#print what to do
hanoi(5,'a','b','c')

#recursive solved this is so few lines!!!  -vs while or for loop (iteratively)

#write recursive code to convert...
