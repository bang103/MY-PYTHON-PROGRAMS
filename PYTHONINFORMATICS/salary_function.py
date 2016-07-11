#Rewrite your pay computation with time-and-a-half for overtime
#and create a function called computepay which takes two parameters (hours and
#rate).
#Enter Hours: 45
#Enter Rate: 10
#Pay: 475.0

import sys
def computepay(hours, rate):
        if hours > 40:
                overforty=hours-40
                extrahours=overforty*1.5
                salary=hours* rate + extrahours*rate
        else:
                salary = hours* rate
        return salary     
        
print 'Program to Calculate salary, given hours of work and rate \n'
print 'Hours above 40 become 1.5 times \n'

try:
        h=raw_input('Enter number of hours worked \n')
        hours = float(h)
except:
        print 'Invalid Input!!! Enter a numeric quantity for number of hours worked \n'
        sys.exit()

try:
        r=raw_input('Rate per hour \n')
        rate=float(r)
except:
        print 'Invalid Input!!! Enter a numeric quantity for rate \n'
        sys.exit()

salary = computepay(hours, rate)
print 'Salary: ',  salary
