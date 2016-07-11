#August 10, 2015
#http://www.cse.msu.edu/~cse231/PracticeOfComputingUsingPython/
#Takes 2 inputs: order of square and starting number
#Outputs latin square
##In my previous programs, I have used sys.exit on catching exceptions, not necessary!!
##Just continue and give user a chance to input correct values

from __future__ import print_function
while True:
    inp1=raw_input("Input the order of the Latin Square--->  ")
    inp2=raw_input("Input the starting number of Latin Square--->  ")
    try:
        order=int(inp1)
        start=int(inp2)
    except:
        print ("The order of square and the starting numbers should be INTEGERS!")
        print ("Please try again")
        continue
    if start>order:
        print ("The starting number should be <= order of the square")
        continue
    rowstart=start
    for i in range (order):
        for i in range(rowstart,order+1):
            print (i,sep=" ", end=" ")
        for i in range(1,rowstart):            
            print (i, sep=" ", end=" ")

        print ("\n", end = "")#to get a newline at the end of each line, without adding additional blank line

        if rowstart==order:
            rowstart=1
        else:
            rowstart +=1
    while True:
        answer=raw_input("Do you want to continue Y/N---->  ")
        if answer.lower() == "y" or answer.lower() == "n": break
        else:
            print (" Must input y/Y to continue or n/N to stop ---->  ")
            continue

    if answer.lower()== "y": continue
    elif answer.lower()=="n": break
           
           
    
    
print ("Bye! Thank you for playing..")
