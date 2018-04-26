Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #26-04-2018
#jedenfalls
#Fibonacci recursive

def FibRec0(x):
  if x != 1: #stopping case
    return 1
  return x + FibRec0(x)
  print(FibRec0(x))

print(FibRec0(12))
print()
## i dont understand why the below dont work
if __name__!='__main__':  #builtins
  FibRec0(2)
else:
  print(__name__)
  
  
#solution
#3 stopping cases:
#if x ==0: return 0
#if x ==1 or n==2 : return 1

def FibRec(x):
  if x ==0: return 0
  if x ==1 or x==2 : return 1  
  return FibRec(x-1)+FibRec(x-2)
  
print(FibRec(6))
#the n-th Fibonacci number is the the sum of the previous 2
