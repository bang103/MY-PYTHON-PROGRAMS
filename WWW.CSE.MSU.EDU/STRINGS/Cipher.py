#http://www.cse.msu.edu/~cse231/PracticeOfComputingUsingPython/
#implements encoding as well as decoding using a rotation cipher
#prompts user for e: encoding d: decoding or q: Qui

import sys
alphabet="abcdefghijklmnopqrstuvwxyz"

print "Encoding and Decoding strings using Rotation Cipher"

while True:
    output=list()
    inp=raw_input("Input E to encode, D to decode and Q to quit--->  ")
    if inp.lower()=="e":            #encode
        while True:                 #input rotation
            inp2=raw_input("Input the rotation: an integer between 1 and 25 --->  ")
            
            if inp2.isdigit()== False:
                print " !!Error: Non digits!! The roatation is a whole number between 1 and 25"
            elif int(inp2)>=1 and int(inp2)<=25:
                rotation=int(inp2)
                break
            else:
                 print " Error! The roatation is a whole number between 1 and 25"
                 
        
        
        cipher = alphabet[rotation:]+ alphabet[:rotation]
                
        instring=raw_input("Input string to be encoded--->  ")
        for char in instring:
            if char in alphabet:
                index=alphabet.find(char)
                output.append(cipher[index])
            else:
                output.append(char)
        outputstring = "".join(output)
        print "The encoded string--->  ",outputstring

    elif inp.lower()=="d":          #decode and find rotation
        instring=raw_input( "Enter string to be decoded--->  ")
        word=raw_input( "Enter a word in the original(decoded) string --->  ")
        rotation=0
        found=False
        for char in alphabet:
           output=list()
           rotation +=1
           cipher=alphabet[rotation:]+alphabet[:rotation]
           
           #decode encoded text with current rotation
           for ch in instring:
               if ch not in cipher:
                   output.append(ch)
               elif ch in cipher:
                   index=cipher.find(ch)
                   output.append(alphabet[index])
           outputstring="".join(output)
       
           if word in outputstring: #IMPORTANT: This statement works only if we join the list into a string
               found=True
               break
           else: continue
        if found == True:
            print "The rotation is %d"%(rotation)
            print "The decoded string is --->  ", outputstring
        else:
             print "Cannot be decoded with rotation cipher: try another sentence"
                               
    elif inp.lower()=="q":
        print "Bye! See you soon"
        break
    
        
