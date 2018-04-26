Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #26-04-2018
#jedenfalls
#recursive tree 

def prefixSumRec(arr):
  if len(arr)==0 or len(arr)==1:
    return arr
  y = prefixSumRec(arr[:-1])
  y.append(y[-1]+arr[-1])
  return y


print(prefixSumRec([1,2,3]))

## i dont understand why the below dont work
if __name__!='__main__':  #builtins
  prefixSumRec([1,2,3,4])
else:
  print(__name__)
