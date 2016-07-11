#Leap year finder
#Leap years occur according to the following formula:
#a leap year is divisible by four, but not by one hundred, unless it is divisible by four hundred.
#For example, 1992, 1996, and 2000 are leap years,
#but 1993 and 1900 are not. The next leap year that falls on a century will be 2400.
#
#Input
#Your program should take a year as input.
#Output
#Your program should print whether the year is or is not a leap year.
#Sample Session
#What year: 1999
#1999 is not a leap year.
#What year: 1988
#1988 is a leap year.
import sys

print 'You can find out if your input is a Leap Year....or not :-) \n'

while True:
        try:
                inp=raw_input( 'Input 4 digit year...Cntrl C if done \n')
        except:
                print "See you next time"
                raw_input( "Press any key to exit--->")
                sys.exit()
                
        try:
                inputyear = int (inp)
        except:
                print "You must enter a 4 digit number for the year, try again"
                raw_input("Press any key to end--->")
                sys.exit()

        if inputyear<1000:
                print "Invalid input: you must input a 4 digit number > 1000"
                continue
        
        if int(inputyear) % 4 != 0:
            print 'Not a leap year \n'
        else:
            if int(inputyear) % 100 == 0:
                if int(inputyear) % 400 == 0:
                    print ' LEAP YEAR!! \n'
                else:
                    print 'Not a leap year \n'
            else:
                print ' LEAP YEAR!! \n'
             


        


