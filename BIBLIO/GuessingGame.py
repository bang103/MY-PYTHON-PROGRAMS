#Guessing game
#The computer will pick a number between 1 and 100. (You can choose any high number you want.) The purpose of the game is to guess the number the computer picked in as few guesses as possible.
#Input
#The user will enter his or her guess until the correct number is guessed.
#Output
#The program will keep asking the user to guess until he or she gets the number correct. Then the program will print how many guesses were required.
#Sample session
#Time to play a guessing game.
#Enter a number between 1 and 100: 62
#Too high. Try again: 32
#Too low. Try again: 51
#Too low. Try again: 56
#Congratulations! You got it in 4 guesses.

import random
print 'Computer will pick a whole number between 1 and hundred and you have to guess it correctly!!'
compnumber= random.randint(1,100)

inputnumber = raw_input('Guess the number! \n')
count=1

while count <= 5 :
    if ( int(inputnumber) - compnumber) < 0 :
        print 'Input a bigger number'
        if  abs(int(inputnumber) - compnumber)< 5:
            print 'but you are very close....\n'
        
    elif ( int(inputnumber) - compnumber) > 0 :
        print 'Input a smaller number'
        if  abs(int(inputnumber) - compnumber)< 5:
            print 'but you are very close....\n'
        
    elif ( int(inputnumber) - compnumber) == 0 :
        print ' Congratulations!!! You got it in ' , count, 'guesses!!! \n'
        raw_input ("Press any key to end-->")
        break
    
    count +=1
    inputnumber = raw_input('Try again..guess the number! \n')
    
if count > 5:
    print 'You have completed 5 tries, no more tries left \n'
    print 'The computer picked', compnumber, '\n'
    raw_input("Press any key to end-->")
