#Rewrite the grade program from the previous chapter using a function
#called computegrade that takes a score as its parameter and returns a grade
#as a string.

#Write a program to prompt for a score between 0.0 and 1.0. If the
#score is out of range print an error. If the score is between 0.0 and 1.0, print a
#grade using the following table:
#Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F

import sys

def computegrade(score):
    if score >= 0.9:
        grade='A'
    elif score >=0.8 and score < 0.9:
        grade = 'B'
    elif score >= 0.7 and  score < 0.8:
        grade = 'C'
    elif score >= 0.6 and score < 0.7:
        grade = 'D'
    elif score < 0.6:
        grade='F'
    return grade

score = 0.0
while score >= 0 and score <= 1.0 :
    try:
        s=raw_input('Enter your score: between 0.0 and 1.0 \n')
        score=float(s)
    except:
        print 'Non-numberic input! enter a number between 0.0 and 1.0 \n'
        sys.exit(1)
        
    print score
    if score <0.0 or score > 1.0:
        print 'Out of range! Enter your score: between 0.0 and 1.0 \n'
        score=0.0
        continue
    else:
        grade = computegrade(score)
        print 'Your Grade: ' , grade
