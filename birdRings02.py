#jedenfalls
#03-02-2019
#birdRings.

#i have thousands of rings
#the rings are only in four colours
#the colours are red (r), blue  (b), green (g) and yellow (y)
#i want to calculate how many unique combinations are possible
#all the combinations require 4 rings
#a colour may be used more than once per combination
#order also matters, so rrrb is different from brrrr
#go

rings = ['r','b','g','y']
z = []

def pickCombo(combo):
  i = 1
 
 #terminationg clause???
  #if len(z)==4:
  #  pass
  #el
  #if len(num)==4:
  #  print("terminating clause reached")
  #  pass
  #el
  if len(combo)==4:
    print("max reached")
    if combo in z:
      print("in z, modifying")
      i=i+1
      #pickCombo(combo)
    else:
      print("not in z, adding branch to z")
      z.append(combo)
      print(z,"\n")
      pickCombo(combo)
  else:
    print("below max, extending branch")
    #yaBokahe = len(combo)
    w = combo.append(rings[i])
    pickCombo(combo)
 
if __name__ == '__main__':
  x = []
  pickCombo(x)
