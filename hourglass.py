Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #26-04-2018
#jedenfalls
#recursive hourglass

#define the problem in terms of itself

#intruction: has to be called hourglass, and has to take string


def hourglass(s):
  #stopping case; 1 letter
  if s:
    if len(s)==1:
      print(s)
    else:
      print(s)
      hourglass(s[:-1])
      print(s)

## i dont understand why the below dont work
if __name__!='__main__':  #builtins
  hourglass("mainman")
else:
  print(__name__)
