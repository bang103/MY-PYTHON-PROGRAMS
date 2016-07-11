#http://www.cse.msu.edu/~cse231/PracticeOfComputingUsingPython/
#Ancient Egyptian Multiplication
##Crazy computer says -3//2 is -2, big problem if second operand is negative, because oper2 is being checked all the time
#also if  second operand has minus sign,then difficult to compute sign of product
#so did whole Egyptian multiplication without signs, using absolute values of the integers
#August 6, 2015

import sys


print "This program multiples two Integers by the Ancient Egyptian Method"
print "Only multiplication and division by 2, and addition are used"
print " No need to remember multiplication tables :-)"

while True:
    listA=list()
    listB=list()
    product=list()
    print "Only multiplication of *integers* is supported"
    inp1=raw_input("Input the first integer -->")
    inp2=raw_input("Input the second integer -->")
    if ("." in inp1) or ("." in inp2) :
        print "Invalid input! Only integer multiplication allowed."
        continue
    try:
        oper1=int(inp1)
        oper2=int(inp2)
    except:
        print "Invalid input! Only numeric(Integer) values accepted"
        sys.exit()

    answer=0
    if oper1==0 or oper2==0: #if either operand is 0
        answer=0
    else:
        #Egyption method starts
        minus=False
        if (oper1<0 and oper2>0)or(oper1>0 and oper2<0): minus=True
        
        oper1=abs(oper1)
        oper2=abs(oper2)
        
        while oper2//2 >0:
            if oper2%2 != 0:
                product.append(oper1)
            oper1 *=2
            oper2 = oper2//2
            print oper1, " " , oper2," " ,product
            
        if abs(oper2)%2 != 0:
                product.append(oper1)
                
        answer=sum(product)
        if minus: answer= -answer
    
    print "The product of %s and %s is %d"%(inp1, inp2, answer)

    cont=""
    while True:
        cont=raw_input("Do you want to continue Y/N")
        if cont.lower()=="y": break
        elif cont.lower()=="n":
            print ("Bye, see you soon")
            sys.exit()
        else: continue
    
    
        


    
