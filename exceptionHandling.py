#jedenfalls
#07-May-2018
#exception error

#types of errors: IOError, NameError, TypeError, ValueError, ZeroDivisionError, IndexError [http://docs.python.org/y3k/library/exceptions.html]

try:
  #x=50/0
  f=open(filename,'r')
  lines.append(f.readline())
  lines.append(f.readline())
  lines.append(f.readline())
  f.close()
    for line in lines:
    print(line)
  f.close()
  
except IOError:
  print("It seems that the file",filename,"does not exist.")
except:
  print("Some other error occurred!")
finally: #this will happen whether or not an error occurred
  print("Executing finally clause")
