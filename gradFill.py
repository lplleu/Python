#grad_fill
#190418
#jedenfalls

def grad_fill(matrix):
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      matrix[i][j]=i+j


X = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

grad_fill(X)

for row in X:
  for col in row:
    print(col,end=' ')
  print()