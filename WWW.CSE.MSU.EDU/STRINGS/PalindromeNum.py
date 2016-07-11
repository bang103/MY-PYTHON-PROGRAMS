#http://www.cse.msu.edu/~cse231/PracticeOfComputingUsingPython/
#September 9, 2015
#
from __future__ import print_function

#take in lower limit
#take in upper limit
#internally keep 3 counters; palindrome, non-lycheral, lycheral
#from lowerlimit to upper limit
    #1.check if number is palindrome, if yes, increment counter, continue
    #2. check for lycheral number: a separate function that takes the number as input
    #keep count of iterations, if > 60 return false else if palindrom is formed
    #return True

palcount=0
lycount=0
non_lycount=0

def ispalindrome(num):
    tmpstr=str(num)
    reverse=tmpstr[::-1]
    if tmpstr==reverse:
        return True
    else: return False

def isnon_lycheral(number):
    count=0
    num=number
    for count in range(60):
        tmpstr1= str(num)
        tmpstr2=tmpstr1[::-1]
        sum=int(tmpstr1)+int(tmpstr2)
        if ispalindrome(sum):
            return True
        else:
            num=sum
    return False
  


    
#main program

print("Palindromes, Lycheral and non-Lycheral numbers")
while True:
    inp1=raw_input("Input a positive integer: Start of range of numbers to check --->")
    if not (inp1.isdigit()):
        print("Invalid input: only positive integers accepted! Try again")
        continue
    
    inp2=raw_input("Input a positive integer: End of range of numbers to check --->")
    if not (inp2.isdigit()):
        print("Invalid input: input both integers again!")
        continue
    
    if int(inp1)<int(inp2): break
    else:
        print("Invalid input: First integer should be < second integer!")
        print("Now input both integers again!")
        continue

#start processing each number
for number in range(int(inp1), int(inp2)+1):
    if ispalindrome(number):
        palcount +=1
        continue
    if isnon_lycheral(number):
        non_lycount +=1
    else:
        lycount +=1
        print("%d is a lycheral number"%number)
        continue

print("In the range %d to %d both inclusive"%(int(inp1), int(inp2)))
print("There are %d Palindromes"%palcount)
print("There are %d Lycheral numbers"%lycount)
print("There are %d Non-Lycheral numbers"%non_lycount)

    
    
    
    
