#http://www.cse.msu.edu/~cse231/PracticeOfComputingUsingPython/
#September 1, 2015
#Will play with inbuilt key, will not prompt for key

from __future__ import print_function
KEY="8765"

def check_repeat(inp):
    for i in range (len(inp)):
        for j in range (i+1, len(inp)):
            if inp[i]==inp[j]:
                return 0
    return 1
    
    


#process_input(inp) compares user input with the key and returns a tuple with 3 items
#1. String Exactly Match=1, else 0
#2. Position: 1-4: indicates how many of the 4 numbers exist in KEY
#    and are at CORRECT POSITION
#3. Exist: 1-4: indicates how many of the 4 numbers exist in KEY
#    but are NOT at correct position
   
def process_input(inp):
    correct =0
    exists=0
    if inp==KEY:
        return (1,4,0)
    else:
        for char in inp:
            if char in KEY:
                if inp.find(char)==KEY.find(char):
                    correct+=1
                else: exists +=1
        return[0,correct,exists]
                
        
    
#val_input() checks if
    #1. input is digits only
    #2. has exactly 4 digits
    #3. all unique numbers i.e. no repeats
#returns input
def val_input():
    while True:
        inp=raw_input("Your guess: ")
        if inp.isdigit()== False:
            print("Invalid guess!! Guess a 4 digit number, non-repeating digits")
            continue

        if len(inp)!= 4:
            print("Invalid guess!! Guess a 4 digit number, non-repeating digits")
            continue

        flag=check_repeat(inp)
        if flag == False:
            print("Invalid guess!! Guess a 4 digit number, non-repeating digits")
            continue
        else:
            return inp
          

#Main Program
print("Welcome to Mastermind")
print("You have 12 guesses to guess the secret 4 digit number: let's play!")
tries=1
trylist=list()

while True:
    inp=val_input()
    tmplist=process_input(inp)
    if tmplist[0]==1:
        print("Congratulations! You have guessed the correct number in %d tries."%tries)
        print("Thank you for playing")
        break
    else:
        tmplist[0]=inp
        trylist.append(tmplist)
        for item in trylist:
            print(item[0], ", Correct: %d, Exists: %d"%(item[1], item[2]))
        tries +=1
        if tries > 12:
            print("Game end! Sorry! you have completed 12 tries. Do try again, bye")
            break
        else:
            continue
