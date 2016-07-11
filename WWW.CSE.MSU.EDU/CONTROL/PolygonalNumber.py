#August 12, 2015
#http://www.cse.msu.edu/~cse231/PracticeOfComputingUsingPython/


from __future__ import print_function
import math
print("On input of a perfect square, Output the two triangles that make up the square.")

while True:
    inp=raw_input("Input Q/q to Quit OR Input a perfect square --->  ")
    try:
        fnumber=float(inp)
    except:
        if inp.lower()=="q":
            print("Bye and Thank you")
            break
        else:
            print("Invalid input: input contains non-numeric characters")
            continue
        

    inp2=str(fnumber)
    index=inp2.find(".")
    
    dec=inp2[index+1:]

    if int(dec)==0:         #a positive integer has been input
        sqnumber=int(fnumber)
        root=int(math.sqrt(fnumber))
        n=root
        t1=int((n*n+n)/2)
        t2=int(((n-1)*(n-1)+(n-1))/2)
        print ("The Square Number %d is made up of Two Triangular numbers %d and %d"% (sqnumber,t1,t2))        
    else:
        print("Invalid input: only perfectly square positive integers accepted")
        continue
    
