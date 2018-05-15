#jedenfalls
#14-05-2018
#quicksort by Sir Charles Anthony Richard Hoare

def swap(values,source,dest):
  """Exchange source and dest values in list"""
  values[source],values[dest]=values[dest],values[source]
  
def partition(values,start,stop):
  """Partition list in-place on last value as pivot"""
  pivot = values[stop] #start with pivot at end 
  midpoint = start
  for position in range(start,stop):
    if values[position]<=pivot:
      swap(values,position,midpoint)
      midpoint+=1
  swap(values,midpoint,stop) #move pivot to middle
  return midpoint
  
def quick_sort2(values,start,stop):
  """Sort values from start to stop using quicksort algorithm"""
  if stop>start:
    pivot = partition(values,start,stop)
    quick_sort2(values,start,pivot-1)
    quick_sort2(values,pivot+1,stop)
    
def quick_sort(values):
  """sort values using quicksort algorithm"""
  quick_sort2(values,0,len(values)-1)
  return values
  
print(quick_sort([2,1,8,0,9,3,15,7]))



