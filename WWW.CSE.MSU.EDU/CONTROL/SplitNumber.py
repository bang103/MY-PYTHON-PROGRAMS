#August 12, 2015
#http://www.cse.msu.edu/~cse231/PracticeOfComputingUsingPython/
from __future__ import print_function

print("Program determines whether given whole number can be cut evenly into specified number of pieces")

while True:
    inp=raw_input("Input a positive integer or Q/q to Quit--->  ")
    if inp.lower()=="q":
        print("Bye and Thank you!")
        break

                            #main program
    elif inp.isdigit():
                          
        while True:     #first get an input for how many digits make up a slice
            inp2=raw_input("How many digits make up each slice? --->  ")
            if inp2.isdigit(): break
            else:
                print("Invalid input:: input a positive integer")
                continue    

        number=int(inp)
        numslice=int(inp2)
        
       
        if (len(inp))%numslice !=0:
            print("%d cannot be split evenly into %d digit slices"%(number,numslice))
            continue
        else:
            print("%d can be split evenly into %d digit slices"%(number,numslice))
            slicelist = list()
            index=0
            while index in range(len(inp)):
                eachslice=inp[index:index+numslice]
                slicelist.append(int(eachslice))
                index +=numslice
            print (slicelist, sep=",", end=" ")
            
            #NOTE: tried printing slicelist using list indices in range(len(slicelist))
            #weird error, also prints the fist element again at the end


            #create a new list with has slicelist items in ascending order
            #then compare it with slicelist

            newlist=list()
            tmplist=list()

            #WARNING: REMEMBER NORMAL LIST BEHAVIOUR
            #assigning one list to another, they point to same list
            #so purpose not served in this case because we want to retain slicelist
            #while tmplist will  eventually become an empty list
            
            for i in range(len(slicelist)):
                tmplist.append(slicelist[i])

            while len(tmplist)>0:
                least=min(tmplist)  
                minindex=tmplist.index(least)   #find index of smallest number
                removed=tmplist.pop(minindex)   #remove that number from slicelist
                newlist.append(removed)         #append that number to newly created list
            
            if newlist==slicelist:
                print (" - increasing order")
            else:
                print (" - not in increasing order")
             
        continue #sliced a number! now prompt user for more numbers to slice


    #prompt for invalid input
    else:
        print("Invalid input::: try again")
        continue
