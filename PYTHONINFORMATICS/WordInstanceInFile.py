#counts the number of times an word appears in a file
#Worked out example
#strips each word of its punctuation and converts to lowercase to get a very accurate answer

import string

print "This program counts the number of times an word appears in a file\n"
file=raw_input("Enter the name of the file:")

DWdCounter=dict()
try:
    handle=open(file,"r")
except:
    print "%s cannot be opened or does not exist"%file
    exit()
    
for line in handle:
    words=line.split()
    for word in words:
        sword = word.translate(None,string.punctuation).lower()
        DWdCounter[sword]=DWdCounter.get(sword,0)+1

handle.close()


#To find the most frequent word, i.e. highest of the values in key:value pair
#http://stackoverflow.com/questions/16569502/get-the-key-correspond-to-maxvalue-in-python-dict

maximum=max(DWdCounter.values())
keys=[x for x,y in DWdCounter.items() if y==maximum]
print keys, " occur with maximum frequency in the text file %s"%(file)


#prints dictionary in ascending order of values, check out key=DWdCounter.get
#http://www.pitt.edu/~naraehan/python2/sorting.html

for word in sorted(DWdCounter,key=DWdCounter.get, reverse=True):
    print word, DWdCounter[word]


#prints dictionary in alphabetical order of keys
#for word in sorted(DWdCounter.keys()):
#   print word, DWdCounter[word]
