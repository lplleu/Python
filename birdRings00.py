# continuation of what I did yesterday in php
# 08_March_19
# jedenfalls

colours = ['r','y','b','s']

def go(world):
   if len(world)==0:
      pass
   else:
      for i in world:
         print i
      go(world[:-1])


if __name__ == '__main__':
   go(colours)
else:
   print __name__
