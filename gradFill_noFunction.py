#gradFill
#199418
#jedenfalls

mat = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

for x in range(len(mat)):
  for y in range(len(mat[x])):
    print(y+x,end="")
  print()