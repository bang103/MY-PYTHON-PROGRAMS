#collects distinct words of a file romeo.txt in a list and then alphabetically orderes the list before printing
#Exercise 8.4 in Lists Chapter, Python for Informatics

import string
filename = "Romeo.txt"

try:
    fhand=open(filename,"r")
except:
    print "File %s does not exist"%(filename)
    exit()
    
ListOfWords=[]
for line in fhand:
    if len(line) == 0: coninue
    line.translate(None, string.punctuation)
    line=line.lower()    
    Words=line.split()
    for word in Words:
        if word in ListOfWords: continue
        else:
            ListOfWords.append(word)
    
print sorted(ListOfWords)
fhand.close()
        


