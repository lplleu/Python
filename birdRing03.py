
numbers = [0,0,0,0]

def on(j):
  if numbers[j]==4:

    #why is he following not working?????

    numbers[j]=numbers[j]
    print(numbers[j])
    pass
  else:
    numbers[j] = numbers[j]+1
    print(numbers)
    on(j)



def go(i):
  if sum(numbers) == 16:
    pass
  elif i==-1:
    i == 3
    go(3)
  else:
    numbers[i] = numbers[i]+1
    print(numbers)
    print("\nrunning 'on'")
    on(i)
    print("\nrunning 'go'")
    go(i-1)




if __name__ == "__main__":
  print("\n")
  print(numbers)
  print("\nstarting with 'go'")
  go(3)
  #on(3)
else:
  print(__name__)

  
