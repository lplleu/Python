#jedenfalls
#07-May-2018
#hat recursion

#recursion is like a russian doll

#key: triangle above me shifted by 1 space

def hat(text,shift=''):
  #stopping, case
  if len(text)>0:
    hat(text[1:-1],shift+' ')
    print(shift+text)
    

if __name__ == 'builtins':
  hat("moodle has been killing the game")
else:
  print(__name__)
