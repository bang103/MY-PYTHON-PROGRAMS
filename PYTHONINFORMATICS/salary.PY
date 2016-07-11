#prompts user for number of hours and hourly rate
#increases rate to 1.5 times if more than 40 hours worked
#computes salary
#

import sys
try:
        hours=raw_input("Enter the number of hours worked:")
        inthours =int(hours)
# inthours =int(hours) should be in try block
#only then exception will be thrown
#import sys and sys.exit() will terminate program

except:
        print 'invalid input please enter numberic value for number of hours'
        sys.exit(1)   

try:       
        rate=raw_input("Enter the rate per hour:")
        floatrate = float(rate)   
except:
        print 'invalid input please enter numberic value for rate'
        sys.exit(1)
        
     
if  inthours>40:
        extrahours=inthours - 40
        #print extrahours
        extrarate= 1.5*floatrate
        #print extrarate
        salary=40*floatrate+extrahours*extrarate
else:
        salary=inthours*floatrate

print "Salary", salary




