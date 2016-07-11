#http://www.cse.msu.edu/~cse231/PracticeOfComputingUsingPython/
#Implement a calculator

import sys
print "Calculator"
print "Adds, subtracts multiplies and divides"
print "On the prompt, enter the operation to be performed"
print " The numbers and the operator must be separated by blank space"


while True:
    answer=0 
    inp=raw_input("Enter the operation--->")
    inplist=inp.split()
    try:
        if inplist[0].find("."):
            num1=float(inplist[0])
        else:
            num1=int(inplist[0])
            
        if inplist[2].find("."):
            num2=float(inplist[2])
        else:
            num2=int(inplist[2])
    except:
        print "Only integer or floating point numbers are accepted"
        print "The numbers and the operator must be separated by blank space"
        print "Exiting application, try again"
        sys.exit()
         
    if inplist[1]=="+":
        answer=num1+num2
    elif inplist[1]=="-":
        answer=num1-num2
    elif inplist[1]=="*":
        answer=num1*num2
    elif inplist[1]=="/":
        if num2==0:
            print "Cannot divide by zero!"
            continue
        else:
            answer=num1/num2
    else:
        print "Wrong operand...try again"
        continue
    print inp, " = ", answer
    
    while True:
        yesno=raw_input("Do you want to continue? Y/N___>")
        if yesno.lower()=="y":
               break
        elif yesno.lower()=="n":
            print "Bye, see you soon"
            print sys.exit()
        else: continue
           
   
