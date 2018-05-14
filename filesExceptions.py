#jedenfalls
#14-05-2018
#outputFirstLine with error exceptions

#import os.path
#if os.path.isfile(filename)

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
