#http://www.cse.msu.edu/~cse231/PracticeOfComputingUsingPython/
#August 19, 2015
#you have to find the shift by finding most commonly occuring characters in order
#of frequency E, T and A

from __future__ import print_function

alphabet="abcdefghijklmnopqrstuvwxyz"

print("Cracking The Caesar Cipher")

while True:
    try:
        chand=open("crackcaesarcipher.txt","r")
        break
    except:
        raw_input("Locate file: crackcaesarcipher.txt..then press any key to continue--->  ")
        continue


# create a dictionary containing frequency of each letter of the alphabet
char_dict=dict()
for line in chand:
    line=line.strip()
    for char in line:
        if char != " ":
            char_dict[char.lower()]=char_dict.get(char.lower(), 0)+1
            
chand.close()


#create a dictionary max_freq containing 3 characters with maximum three frequencies
max_freqency=dict()
count=0
for item in sorted(char_dict,key=char_dict.get, reverse=True):
    
    max_freqency[item]=char_dict[item]
    count +=1
    if count==3: break


#find shift of e-eshift; check whether 't' and 'a' are obtained if next two frequently appearing characters
#are shifted by eshift
#then you can conclude that the shift is correct
#GOT MY HEAD COMPLETELY TWISTED BECAUSE OF WRAP ROUND
count=0
for item in sorted(max_freqency, key=max_freqency.get, reverse=True):
    if count == 0:
        eshift=ord(item)-ord('e')
        if eshift==0: print("This text is not encrypted!")
        elif eshift<0: eshift +=26
    if count == 1:
        tpos=ord(item)-eshift
        if tpos < ord('a'): tpos += 26
    if count == 2:
        apos = ord(item)-eshift
        if apos<ord('a'): apos += 26
    count +=1

#like the alphabet string, make a cipher string, with alphabets shifted, map from cipher to alphabet by position in string
if chr(tpos)=='t' and chr(apos)=='a':
    cipher=alphabet[eshift:]+alphabet[:eshift]
   

while True:
    try:
        chand=open("crackcaesarcipher.txt","r")
        break
    except:
        raw_input("Locate file: crackcaesarcipher.txt..then press any key to continue--->  ")
        continue 

outhand=open("decrypted.txt","w")

for line in chand:
    line=line.strip()
    outlist=list()
    for char in line:
        if char in cipher:
            position=cipher.index(char)
            outlist.append(alphabet[position])
        elif char not in cipher:
            outlist.append(char)
    outlist.append("\n")
    outstring="".join(outlist)
    outhand.write(outstring)

    
chand.close()
outhand.close()

    
