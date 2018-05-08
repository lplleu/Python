#jedenfalls
#08-05-18
#linear search

def linear_search(arr,query):
    """Search sequentially"""
    for i in range(len(arr)):
        if arr[i]==query:
          return i
        return -1 # means NOT FOUND
    
if __name__ == 'builtins':
  print("found something")
  linear_search([1,2,3,4,5],2)
else:
  print("nothing.")

#done in a recursive manner

#stopping cases:
  #empty (not there) or array_lenght == 0 >> rerturn -1
  #if last item == query >> return len(arr)
  
  #otherwise return the recursive call
  
#def linear_search_rec(arr,query):
