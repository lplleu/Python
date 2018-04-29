#jedenfalls
#29-04-2018
#pyramid, finally.

def hourglass(x):
  if len(x)==0:
    pass
  elif len(x)==1:
    print(x[0:1])
  elif len(x)>1:
   print(x)
   hourglass(x[:-1])
   print(x)
  
if __name__ == 'builtins':
  hourglass("tomorrow")
else:
  print("represent")
