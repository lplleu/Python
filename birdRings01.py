#jedenfalls
#03-02-2019
#pyramid, finally.

#i have thousands of rings
#the rings are only in four colours
#the colours are red (r), blue  (b), green (g) and yellow (y)
#i want to calculate how many unique combinations are possible
#all the combinations require 4 rings
#a colour may be used more than once per combination
#order also matters, so rrrb is different from brrrr
#go

rings = ['r','b','g','y']

import random  

def pickCombo(combo):
  if len(combo)==4:
    print(combo)
    pass
  else:
    i = random.randint(0,3)
    combo.append(rings[i])
    pickCombo(combo)

if __name__ == '__main__':
  for y in range(5):
    x = []
    pickCombo(x)
