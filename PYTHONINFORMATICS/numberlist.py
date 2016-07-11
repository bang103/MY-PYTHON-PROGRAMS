#Write a program which repeatedly reads numbers until the user enters
#done
#print out the total, count, and average  maximum and minimum of the numbers
#
#If the user enters anything other than a number, detect their mistake
#using try and except and print an error message and skip to the next number.

import sys

count = 0
total=0.0
average=0.0
maximum=0.0
minimum=0.0


userinput=raw_input('Enter a number or enter DONE when you are done \n')
while userinput.isdigit() or (userinput.isalpha() and userinput.lower() != "done"):
    if userinput.isdigit():
        count=count+1
        currentnumber=float(userinput)
        total=total+currentnumber
        if currentnumber > maximum:
            maximum = currentnumber
        if count == 1:
            minimum=currentnumber
        else:
            if currentnumber < minimum:
                minimum=currentnumber
    else:
         print 'Invalid input! Enter a number or enter DONE when you are done \n'
    userinput=raw_input('Enter a number or enter DONE when you are done \n')

if count >0:
    average=total/count
print '\n'
print 'Count: ' , count, '\n'
print 'Total : ', total,  '\n'
print 'Average : ', average, '\n'
print 'Maximum : ', maximum, '\n'
print 'Minimum : ', minimum,  '\n'

    
