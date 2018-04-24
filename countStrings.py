#dictionaries
#24-04-2018
#jedenfalls
x = [1,2,3,4] #array
y = {}
y["apples"]=2
d = {"man":24,"woman":"again","child":"kind"}
#print(x)
#print()
#print(y)
#print()
#print(d)
###########print(d.keys)
#print()
#iterating through a dictionary gives the keys, vs values
#for i in d:
# print(i)
#print()
#vs
#for i in x:
# print(i)
# which gives the values
#print()
#to print the values in a dictionary, we use syntax
#for i in d:
#print(d[i])
text ="It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him.The hallway smelt of boiled cabbage and old rag mats. "

def CountW(textToAnalyse):
    wordList=textToAnalyse.split()
    #print(wordList)
    
    words0={} #this means 'a dictionary'
   
    #step through each word in the list
          for i in wordList:
              i=i.lower() #for comparability
              i=i.strip(".,!?") #remove punctuation
              if i in words0:
                 words0[i]+=1
              else:
                   words0[i]=1
                   for i in sorted(words0): #added sorted since this uses hash
              print(i,"occurs",words0[i],"times.")

if __name__ == '__main__':
   pass
else:
     CountW(text)
