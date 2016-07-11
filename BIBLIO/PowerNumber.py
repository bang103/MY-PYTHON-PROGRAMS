#Powerball number generator
#Description follows program
#July 31, 2015

from __future__ import print_function
import sys
import random

def generate():
    powerlist=list()
    for i in range(5):
        powerlist.append(random.randint(1,53))
    powerlist.append(random.randint(1,42))
    print("Powerball numbers: ", end=" ", sep = " " )
    for i in range(5):
        print(powerlist[i], end=" ", sep = " ")
    print("     Powerball: ",powerlist[len(powerlist)-1])
    


#main    
print("Powerball Lottery number generator")
inp=raw_input("How many sets of powerball numbers do you want?")
try:
    num=int(inp)
    
except:
    print("Please enter a *number*, how many sets of powerball numbers?")
    sys.exit()

for i in range(num):
    generate()
raw_input("Press any key to close window--->")

#Description
#To win the Powerball lottery (an extremely unlikely event so don't waste your time)
#you have to pick six numbers correctly. The first five numbers are drawn from a drum containing 53 balls and the sixth is drawn from a drum containing
#42 balls. The chances of doing this are 1 in 120,526,770.
#Write a program to generate a set of Powerball numbers by utilizing the choice function in Python's random module.
#Input
#Ask the user how many sets of Powerball numbers he or she would like.
#Output
#The program will print each set of Powerball numbers in numeric order.
#Sample session
#Official (but fruitless) Powerball number generator
#How many sets of numbers? 3
#Your numbers:  3 12 14 26 47     Powerball:  2
#Your numbers:  1  4 31 34 51     Powerball: 17
#Your numbers: 10 12 49 50 53     Powerball: 35
