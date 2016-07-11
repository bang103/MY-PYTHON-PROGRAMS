#Exercise 8.6 in Python Informatics
#Prints out the email ids of the senders

filename="mbox-short.txt"
try:
    fhand=open(filename, "r")
except:
    print "File %s does not exist"%(filename)
    exit()
ListOfPeople=[]
for line in fhand:
    if len(line)== 0: continue
    if line.startswith("From:"): continue
    if line.startswith("From"):
        words=line.split()
        ListOfPeople.append(words[1]) 

for item in ListOfPeople:
    print item

print "There are %d lines beginning with From"%(len(ListOfPeople))
fhand.close()   
