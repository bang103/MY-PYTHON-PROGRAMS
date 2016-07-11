#Exercise 9.1 in Python for INformatics
#Creates a dictioanary using distinct words in a file as keys

import string
filename = "Romeo.txt"

try:
    fhand=open(filename,"r")
except:
    print "File %s does not exist"%(filename)
    exit()
DictWords=dict()
for line in fhand:
    line=line.lower()
    line=line.translate(None, string.punctuation)
    words=line.split()
    for word in words:
        DictWords[word]= DictWords.get(word, 0)+1

print DictWords
fhand.close()
