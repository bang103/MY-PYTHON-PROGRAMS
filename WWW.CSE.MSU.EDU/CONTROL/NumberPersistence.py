#August 12, 2015
#http://www.cse.msu.edu/~cse231/PracticeOfComputingUsingPython/

from __future__ import print_function

print("Progarm to find the additive and multiplicative persistence of a positive integer")
print("Input positive integers, to quit Q/q")

while True:
    inp=raw_input("Input a positive integer or Q/q to Quit--->  ")
    if inp.lower()=="q":    #quit since Q has been input
        print("Bye! Thank you for using this program")
        break
    elif inp.isdigit():     #process valid input
        
        masterinput=int(inp)
        addpersist=0
        multipersist=0
        addroot=masterinput
        multiroot=masterinput

        number=masterinput  #finding out additive persistence and root
        while True:         
            numlist=list()
            tempnum=number
            while tempnum>0:
                rem=tempnum%10
                numlist.append(rem)
                tempnum/=10
            if len(numlist)==1:
                addroot=number
                break
            number=sum(numlist)
            addpersist +=1

        number=masterinput  #finding out multiplicative persistence and root
        while True:         
            numlist=list()
            tempnum=number
            while tempnum>0:
                rem=tempnum%10
                numlist.append(rem)
                tempnum /=10
            if len(numlist)==1:
                multiroot=number
                break
            
            product=1
            for num in numlist:
                product *= num
            number=product
            multipersist +=1


        print("Additive persistence:        %d"%addpersist, end="                   ")
        print("Additive root:    %d"%addroot)
        print("Multiplicative persistence:    %d"%multipersist,end="        ")
        print("Multiplicative root:    %d"%multiroot)
            
            

        
    elif inp.isalnum():     #invalid number so prompt again for input
        print("Invalid input: Only positive integers or Q/q to Quit")
        continue
    
            


    
