Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #26-04-2018
#jedenfalls
#mystery recursive

def mystery(x):
  if x==1:
    return 2
  if x==0:
    return 1
  return 2*mystery(x-1)
  
print(mystery(12))

#answer: gives 2 to specified power


## i dont understand why the below dont work
if __name__!='__main__':  #builtins
  mystery(2)
else:
  print(__name__)
