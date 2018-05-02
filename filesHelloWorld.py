import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

#print(dir_path)

text = "text files are typically ascii or unicode, binaries are not text files but store info in application specific formats (hence not human-readable)"

#syntax
#<file> = open(<filename>,<mode>)
#mode can be 'r' to read, 'w' to overwrite, and "a" to append

f = open('readme.txt','r')
g = f.readline()
h = f.readlines()
i = f.read()
#print(g)

print(g)

words={}
for line in h:
    text = line.split() #this seems to split by character, not space [for readline, ok for readlines]
    for w in text:
       #print("working on",w) --tracing statement
        w=w.strip('.,!" ')
        w=w.lower()
        if w not in words: #because it has not been previously counted
            words[w]=1
        else: 
            #print("working on ",w) --another tracing statement
            words[w]+=1 #increment count

print("the words in the file are:")
for w in sorted(words):
    print(w,words[w])
    
#for key, value in sorted(mydict.iteritems(), key=lambda (k,v): (v,k)):
#    print "%s: %s" % (key, value)

f.close()
