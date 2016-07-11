#Rock, Paper,Scissors
#Description follows
#July 31, 2015

from __future__ import print_function
import sys,random

rps=("", "r", "p","s")

#create a dictionary with rps rules
dictwinner={("r","p"):"p", ("p","r"):"p", ("p","s"):"s",("s","p"):"s", ("s","r"):"r", ("r","s"):"r"}
dictprint={"r":"Rock", "p":"Paper", "s":"Scissors"}
#human and computer scorecard


def whowinsthisround(human,computer):
    print("Human: ",dictprint[human],"    ","Computer: ", dictprint[computer], sep = " ", end=" ")
    if human==computer:
        return "draw"
    else:
        winner=dictwinner[human, computer]
        if winner==human:
            return "human"
        elif winner==computer:
            return "computer"
           
    

#main

hscore=0
cscore=0    
print("Welcome to Rock Paper Scissors!")
inp=raw_input("How many points are required to win?  ")

try:
    towin=int(inp)
except:
    print("Invalid input: you must enter a Whole Number for points required to win.  ")
    print("Start all over again!  ")
    raw_input("Enter any key to exit.....")
    sys.exit()
name=raw_input("What is you name?  ")  

while True:
    try:
        inp=raw_input ("Choose (R)ock, (P)aper or (S)cissors?  ")
    except:
        print("Game interrupted!", end=" ", sep=" ")
        if cscore>hscore:
            print("Computer Wins the Tournament! ")
        print("Bye! See you soon....")
        raw_input("Enter any key to exit.....")
    
    if inp not in "RPSrps":
        print("Invalid input, you must input alphabets r/R, p/P or s/S  ")
        continue
    
#game starts!
    gen=random.randint(1,3)
    winner=whowinsthisround(inp, rps[gen])
    if winner=="human":
        print("     %s wins!"%(name))
        hscore +=1
    elif winner=="computer":
        print("     Computer wins!")
        cscore +=1
    elif winner=="draw":
         print("     It's a Draw")
    print("Score:  %s:"%(name), hscore, "   Computer: ", cscore)     
                  
    if hscore==towin:
        print("Human wins tournament!")
        print("%s: "%(name), hscore,"  Computer: ", cscore)
        raw_input("Enter any key to exit.....")
        sys.exit()
    elif cscore==towin:
        print("Too bad :-( Computer wins the tournament!")
        print("Computer: ", cscore," %s: "%(name), hscore)
        raw_input("Enter any key to exit.....")
        sys.exit()
        
#Description
#Rock, paper, scissors, also know as roshambo, is a simple child's game that is frequently used to settle disputes.
    
#In the game, a rock breaks the scissors, the scissors cut the paper, and the paper covers the rock.
    
#Each option is equally likely to prevail over another.
#If the players choose the same object a draw is declared and the game is repeated until someone prevails.
#For more information than you ever thought it was possible to collect about rock, paper, scissors,
#check out the Web page of the World RPS Society.
#In this computerized version the human player competes against the computer which chooses a rock, paper,
#or scissors randomly. The game proceeds until the human player quits the game or until a predetermined score is reached
#(e.g., 11 pts.) at which time the final tally is displayed. Solutions with fewer numbers of if statements are considered
#more elegant.

#Input
#The human player enters the number of points required for a win. During the play of the game the human player selects whether to play a rock,
#paper, or scissors by using the keyboard. The human player may also end the game by pressing the Control-D sequence at any time.
#(Ending the game early does not allow a winner to be determined if the human player is ahead.)
#Output
#The program will display the winner of each roshambo round along with the running score.
#At the conclusion of the game, the computer will display the overall winner and the final score.
#Sample session
#Welcome to Rock, Paper, Scissors!
#How many points are required for a win? 3
#Choose (R)ock, (P)aper, or (S)cissors? r
#Human: rock    Computer: paper        Computer wins!
#Score: Human 0   Computer 1
#Choose (R)ock, (P)aper, or (S)cissors? r
#Human: rock    Computer: scissors     Human wins!
#Score: Human 1   Computer 1
#Choose (R)ock, (P)aper, or (S)cissors? p
#Human: paper   Computer: paper        A draw
#Score: Human 1   Computer 1
#Choose (R)ock, (P)aper, or (S)cissors? s
#Human: scissors  Computer: paper      Human wins!
#Score: Human 2   Computer 1
#Choose (R)ock, (P)aper, or (S)cissors? r
#Human: rock      Computer: scissors   Human wins!
#Final Score: Human 3   Computer 1
#Going further
#Ask the user for his or her name and use the name while the game is playing.
#Display randomly chosen taunts when the computer wins.
#Consult the World RPS Society Web page and try to program the computer to use some strategy.
