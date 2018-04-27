#countdown
#27042018
#jedenfalls

from functools import lru_cache

@lru_cache(maxsize=1000)

def countdown(x):
    
  if x <= 0:
    return 0
  print(x)
  return countdown(x-1)

if __name__ == 'builtins':
  print(countdown(8))
else:
  print(__name__)
