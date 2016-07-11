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

score=0.0

while score >= 0.0 and score <= 1.0:
    try:
        s=raw_input("Enter your score: between 0.0 and 1.0 \n")
        score=float(s)
    except:
        print 'invalid input,enter number between 0.0 and 1.0 \n'
        sys.exit(1)
    
    if score < 0.0 or score > 1.0:
        print 'invalid input,enter number between 0.0 and 1.0 \n'
        score=0.0
        continue
    else:
        if score >= 0.9:
            print 'Congratulations! You have got an A\n'
        elif score >= 0.8 and score < 0.9:
            print ' Congratulations! You have got a B\n'
        elif score >= 0.7 and score < 0.8:
            print 'You can do better You have got a C\n'
        elif score >= 0.6 and score < 0.7:
            print 'You have to work harder, You have got a D\n'
        elif score <0.6:
            print 'You have failed the test, You have got an F\n'
             
