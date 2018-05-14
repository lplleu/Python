#jedenfalls
#14-05-2018
#outputFirstLine with error exceptions

def search(query,arr): #returns position where the query exists in the file
    for i in range(len(arr)):
        if arr[i]==query:
            return i
    return -1 #if you get to the end of the whole process

fileOK=False
while not fileOK:
    try:
        filename=input("Type in file name:\n")
        dataF=open(filename,'r')
        data = dataF.readlines()
        
        #clean up data
        for i in range(len(data)):
            data[i]=data[i].strip('\n')     
            #data[i]=eval(data[i])
            
        print(data)
        fileOK=True
        dataF.close()
        query=input("type value to search for\n")
        position = search(query,data)
        if position==-1:
            print(query,"not found")
        else:
            print(query,"is in line",position+1,"in the file")
    except IOError as errno: #input-output error (example of named exception)
        #you can also have it in a loop and keep asking for new file names.
        print("File",filename,"does not exist\ncheck line",errno)
    except ZeroDivisionError:
        print("You divided by zero")
    #except IOError:
        #print("File",filename,"does not exist")
    #except IOError:
        #print("File",filename,"does not exist")
    #finally: #happens whether an exception occured or not
        #print("end of code")
print("File exists")

#import os.path
#if os.path.isfile(filename)
