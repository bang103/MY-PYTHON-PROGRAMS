#Hangman
#July 30, 2015
#Description of rules after the program
#TheWord-Word to Guess
#Hangman-List containing hangman parts
#InputWord - Word being formed
#InputChar- character being input everytime
#HMan.txt - file containing words for the hangman game

####the following import disables print statement and enables print inbuilt function


from __future__ import print_function
import sys

#file containing wordlist of 40 words, one on each line
fname="words.txt"

#List containing the parts of Hangman
Hangman = [" ","O\n","\\","|","/\n"," |\n","/"," \\"]
HangLength=7

#Draw the hangman, depending on how many wrong tries, passed as count
def DrawHangman(count):
    print("\n")
    i=1
    for char in Hangman:
        print (char,sep="",end="")
        if i>count: break
        i+=1


#get a word from the file words.txt, which contains 40 words, one on each line       
def getword(num):
    try:
        fhand=open(fname, "r")
    except:
        print("%s, file containing words cannot be opened"%(fname))
        raw_input("Enter any key to exit.....")
        sys.exit()
              
    count=1         
    for line in fhand:
        if count !=num:
            count +=1
            continue
        lst=line.split()
        word=lst[0]
        fhand.close()
        return word

def dispword(someword):
    for i in range(len(someword)):
        print(someword[i],end=" ", sep="  ")
      
        
   
print ("Welcome to Hangman \n")
print ("Guess the mystery word \n")
try:
    num=int( raw_input("Choose a number between 1 and 40, both included to get your word \n"))
except:
    print("Invalid input: You must enter a whole number between 1 and 40 to generate a word")
    raw_input("Press any key to exit.....")
    sys.exit()
if num<1 or num>40:
    print ("Please enter a whole number between 1 and 40 to generate a word\n")
    raw_input("Press any key to exit.....")
    sys.exit()
    
TheWord=getword(num)
Length=len(TheWord)

InputWord=list()
for i in range(len(TheWord)):
    InputWord.append("_")

hangcount=0
charcount=0
GuessList=list()

while True:
    dispword(InputWord)
    InputChar=raw_input("Pick a letter -->")
    if not InputChar.isalpha():
        print("You must input only alphabets!! Pick a letter -->")
        continue
    if InputChar in TheWord:
        index=TheWord.find(InputChar)
        while (index != -1) and index < len(TheWord): #search for multiple instances of aletter, find only returns first instance
            if (InputWord[index]=="_"):
                InputWord[index]=InputChar
                charcount +=1
                break
            else:
                index = TheWord.find(InputChar, index+1, len(InputWord))
                if index == -1 :            #no more instances of that letter, counts as invalid letter        
                    hangcount +=1
           
        GuessList.append(InputChar)
        print("Guessed Alphabets --->",end=" ")
        dispword(GuessList)
        DrawHangman(hangcount)
        print("\n")
    else:
        GuessList.append(InputChar)
        print("Guessed Alphabets --->",end=" ")
        dispword(GuessList)
        hangcount +=1
        DrawHangman(hangcount)
        print("\n")
        
    if (hangcount == HangLength):
        print("Sorry, the hangman strikes!")
        print("The mystery word was %s"%(TheWord))
        raw_input("Press any key to end-->")
        break
    
    if charcount==Length:
        print("Congratulations! You Got it--> %s"%TheWord)
        raw_input("Press any key to end-->")
        break
        








#Description
#Hangman is a popular word guessing game where the player attempts to construct a missing word by guessing one letter
#at a time. After a certain number of incorrect guesses, the game ends and the player loses.
#The game also ends if the player correctly identifies all the letters of the missing word.
#Input
#Your program will prompt the user for letter guesses until the word is correctly guessed or the player has exceeded
#the maximum number of guesses. User input should be checked to make sure it's valid.
#A large file full of words is available for you to use in your program.
#You will certainly need to write some code to filter out the words of a certain length.
#Perhaps you could prompt the player for the length of the word they would like to guess and adjust the number of allowable
#wrong guesses accordingly.
#Output
#Your program should print a list of letters that have been guessed as well as display the correctly guessed letters
#in the word. A graphical representation of the hanging man (kinda gross when you think about it) is optional.
#Sample Run
#Welcome to hangman. You get seven chances to guess the mystery word.
#_ _ _ _ _ _
#Pick a letter --> e
#Guessed letters: E
# O
#_ _ _ _ _ _
#Pick a letter --> a
#Guessed letters: E A
# O
# |
#_ _ _ _ _ _
#
#Pick a letter --> e
#Sorry, you already guessed 'E'
#Pick a letter --> i
#
#Guessed letters: E A I
#
#O
#\|
#_ _ _ _ _ _
#
#Pick a letter --> o
#Guessed letters: E A I O
#
# O
#\|
#
#_ O _ _ _ _
#Pick a letter --> u
#Guessed letters: E A I O U
# O
#\|/
#_ O _ _ _ _
#Pick a letter --> y
#Guessed letters: E A I O U Y
# O
#\|/
#_ O _ _ _ Y
#
#Pick a letter --> 4
#'4' is not a valid letter
#Pick a letter --> xyz
#'XYZ' has more than one letter.
#Pick a letter --> l
#Guessed letters: E A I O U Y L
# O
#\|/
#_ O _ _ L Y
#Pick a letter --> s
#Guessed letters: E A I O U Y L S
# O
#\|/
# |
#_ O _ _ L Y
#Pick a letter --> r
#Guessed letters: E A I O U Y L S R
# O
#\|/
# |
#/
# 
#_ O _ _ L Y
#Pick a letter --> k
#Guessed letters: E A I O U Y L S R K
# O
#\|/
# |
#/ \
# 
#_ O _ _ L Y
#So sorry. You struck out.
#The mystery word was 'COMPLY.'



