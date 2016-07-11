#Try again July 31, 2015
#amount coming weird value

#from decimal import *
#getcontext().prec = 2

print 'Loan Payment Calculator'

p=raw_input('Amount borrowed i.e.Principal amount is  ')
principal = float(p)

r=raw_input('Rate of interest i.e. rate% is  ')
rate=float(r)/100

t=raw_input('Duration of loan in years i.e. time period  is ')
time=int(t)
months=time*12

interest=principal*rate*time
amount =principal+interest

mi=amount/(time*12)

print '  Month   Amount Paid       Remaining Balance '

balance=amount
for i in range(months):
    remaining=balance-mi
    print (i+1),"   ","%.2f"%(mi),"   ", "%.2f"%(remaining)
    balance=balance-mi
raw_input("To close window, press any key--->")

#As of 16 June 2015, NOT DONE, money calculations HEADACHE
#Loan and payment calculator
#The interest due on a loan can be calculated according to the simple formula: I=P*R*T
#where I is the interest paid, P is the amount borrowed (principal), R is the interest rate, and T is the length of the loan.
#It is common for loans to be amortized which allows the lendor to collect their interest early in the loan period.
#We will ignore amortization for the purpose of this program. For bonus points, figure out how to do amortization and print
#an amortization schedule with the payment schedule.
#There is an excellent explanation of the amortization formula at Interest.com.
#
#Write a program that calculates the interest due on a loan and prints a payment schedule.
#Make sure you round the output to two decimal places. For bonus points, figure out how to calculate
#amortization and print an amortization schedule.
#It will be your responsibility to find an appropriate format for the amortization printout.
#
#Make sure you handle the dollars correctly!
#Floating point numbers in Python (and other programming languages) are subject to rouding errors when doing floating
#point arithmetic.
#For an explanation of this phenomenon, see the floating point arithmetic section of the Python tutorial.
#One of the most common strategies to solve the problem is to do all money-related calculations in pennies,
#converting back to dollars when the results
#are displayed. If you don't handle this issSue correctly, your program won't give correct answers in all cases.
#

#Input
#The program will prompt the user for the amount borrowed,
#interest rate as a percentage (in annual interest terms), and the term of the loan in years.
#Output
#The program will print the amount borrowed, total interest paid, the amount of the monthly payment, and a payment schedule.
#Sample session
#Loan calculator
#Amount borrowed: 100
#nterest rate: 6
#Term (years): 1
#Amount borrowed:    $100.00
#Total interest paid:  $6.00

#           Amount     Remaining
#Pymt      Paid       Balance
#-----      -------    ---------
#  0        $ 0.00      $106.00
#  1        $ 8.84      $ 97.16
#  2        $ 8.84      $ 88.32
#  3        $ 8.84      $ 79.48
#  4        $ 8.84      $ 70.64
#  5        $ 8.84      $ 61.80
#  6        $ 8.84      $ 52.96
#  7        $ 8.84      $ 44.12
#  8        $ 8.84      $ 35.28
#  9        $ 8.84      $ 26.44
# 10        $ 8.84      $ 17.60
# 11        $ 8.84      $  8.76
# 12        $ 8.76      $  0.00


    
    
    





