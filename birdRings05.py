# reset n+1, and increment until 4 >> later will do it in reverse
# 15_March_19
# jedenfalls

# output all possible combinations/permutations of a 4 colour
# 15 March 19
# jedenfalls

numbers = [0,0,0,0]

def on(j):
  if sum(numbers) == 16 or numbers[j]>3:
    #print('numbers j is '+str(numbers[j]))
    pass
  else:
      #print('numbers j is '+str(numbers[j]))
      numbers[j] = numbers[j]+1
      if numbers[j] > 4:
        print("PROBLEM HERE 1")
      print(numbers)               #add to x instead of printing?    [x.append(numbers)]
      w = "'".join(str(e) for e in numbers)
      x.append(w)
      on(j)

def reseting(k,m):
   numbers[k+1]=m
   
def go(i):
  if sum(numbers) == 16:
    pass
  elif i==-1:
    i == 3
    go(3)
  else:
    if i<3:
      #print("ONLINE")
      numbers[i+1]=numbers[i+1]-1
      o = numbers[i]+1
      if o>4:
        pass
      else:
        numbers[i]=numbers[i]+1
        q = "'".join(str(e) for e in numbers)
      #print("checking here for "+q)
      
        if q not in x:
         #print(q+" not found -retaining it.")
         
          w = "'".join(str(e) for e in numbers)
          x.append(w)
        else:
         #print(q+" found -incrementing.")
         #print("RUNNING THIS LINE")
          numbers[i+1]=numbers[i+1]+1

    else:
      #print("RUNNING")
      if numbers[i]+1>4:
        pass
      else:
        numbers[i] = numbers[i]+1    # what is this doing?
      if numbers[i] > 4:
        print("PROBLEM HERE 2")
    print(numbers)               # add to x instead of printing?    [x.append(numbers)]
    w = "'".join(str(e) for e in numbers)
    x.append(w)
    m = numbers[i]
    on(i)
    
    numbers[i] = m               # will be working here (m-1) instead of (m)

      
    go(i-1)

if __name__ == "__main__":
  print(numbers)                 #add to x instead of printing?    [x.append(numbers)]
  x = []
  w = "'".join(str(e) for e in numbers)
  x.append(w)
  go(3)
  #print('\n')
  #print(x)
else:
  print(__name__)
  
# changelog

# 16_March_19
# managed to ensure that no values exceed 4
