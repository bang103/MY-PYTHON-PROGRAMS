#http://www.cse.msu.edu/~cse231/PracticeOfComputingUsingPython/
#September 9, 2015
#only numbers up to 380 are supported i.e. even sum should be less than 380
#so operands should be max 190
    
from __future__ import print_function

#returns integer values of each of the symbols 
def toint(symbol):
    if symbol.upper() == "I": return 1
    elif symbol.upper() == "V": return 5
    elif symbol.upper() == "X": return 10
    elif symbol.upper() == "L" : return 50
    elif symbol.upper() == "C" :return 100


def valid_roman(inp):
   
    for char in inp.lower():
        if char in "ivxcl": continue
        else: return False
    return True
        
    
def roman_to_int(roman):
    number = 0
    i=0
    while i < (len(roman) - 1):
        val1=toint(roman[i])
        val2=toint(roman[i+1])
        if val1<val2:
            number +=val2-val1
        else:
            number += val1+val2
        i +=2
    return number
        
def int_to_roman(num):
    
    
#main

print("This program will accept two Roman Numbers and print their sum")
print("** At present,each operand < 190 **")

while True:
    input1=raw_input("Input the first Roman Number -->  ")
    if valid_roman(input1): break
    else:
        print("Invalid input!! Roman numbers upto 380, contain only I,V,X,L or C")
        continue
   
   
    
while True:
    input2=raw_input("Input the second Roman Number -->  ")
    if valid_roman(input2): break
    else:
        print("Invalid input!! Roman numbers upto 380, contain only I,V,X,L or C")
        continue
   
sum=roman_to_int(input1) + roman_to_int(input2)

print("The sum of %s and %s  is %d"%(input1, input2, int_to_roman(sum)))





       
    
