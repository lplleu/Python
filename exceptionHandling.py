#jedenfalls
#07-May-2018
#exception error

#types of errors: IOError, NameError, TypeError, ValueError, ZeroDivisionError, IndexError [http://docs.python.org/y3k/library/exceptions.html]
fileOK=False
while not fileOK:
  try:
    #x=50/0
    inputF=input("type filename")
    
    if inputF=="":
      sys.exit()
    
    f=open(filename,'r')
    lines.append(f.readline())
    lines.append(f.readline())
    lines.append(f.readline())
    f.close()
      for line in lines:
      print(line)
    f.close()
    fileOK=True
  
except IOError as er:
  print(er)
  #print("It seems that the file",filename,"does not exist.")
except SystemExit:
  check=input("quit?")
  if check=="yes":
    print("quiting")
    fileOK=True
except:
  print("Some other error occurred!")
finally: #this will happen whether or not an error occurred
  print("Executing finally clause")
