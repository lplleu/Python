numbers = [0,0,0,0]
###
def on(j):
  if numbers[j]==4:

    numbers[j]=numbers[j]
    pass
  else:
    numbers[j] = numbers[j]+1
    print(numbers)
    on(j)

def reset(k,m):
   if numbers[k]==4:
      numbers[k]=m
      print(numbers)
   else:
      numbers[k] = numbers[k]+1
      print(numbers)
      reset(k,m)

def reseting(k,m):
   numbers[k+1]=m
   
def go(i):
  if sum(numbers) == 16:
    pass
  elif i==-1:
    i == 3
    go(3)
  else:
    n = numbers[i]
    print("\nremembering intial value of column "+str(i)+" which is "+str(n))
    numbers[i] = numbers[i]+1
    print(numbers)
    m = numbers[i]
    #print("\nremembering intial value of column "+str(i)+" which is "+str(m))
    print("\nrunning 'on'")
    on(i)
    #if(i<3):
    #  l = numbers[i+1]
    #else:
    #  l = 0 
    print("\nrecalling column "+ str(i+1))
    numbers[i] = m
    print("\nrunning 'go' for column "+ str(i))
    go(i-1)
    #print("\nrunning 'reset'")
    #reset(i,l)   




if __name__ == "__main__":
  print("\n")
  print(numbers)
  print("\nstarting with 'go'")
  go(3)
  #on(3)
else:
  print(__name__)
