def hanoi(n,source,spare,destination):
  #stopping case
  if n>0: #there is nothing to solve if n==0
    hanoi(n-1,source,destination,spare) #290418 -what is the purpose of "spare" here??????
    print("move disk",n,"from",source,"to",destination)
    hanoi(n-1,spare,source,destination)

#print what to do
hanoi(5,'a','b','c')

#recursive solved this is so few lines!!!  -vs while or for loop

#write recursive code to convert...
