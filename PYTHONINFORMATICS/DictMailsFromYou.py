#Exercise 9.3 from Python Informatics ebook
#Write a program to read through a mail log, and build a histogram
#using a dictionary to count how many messages have come from each email address
#and print the dictionary.
#use mbox-short.txt
#Then modify program slightly to print for Ex. 9.5
#Exercise 9.5 This program records the domain name (instead of the address)
#where the message was sent from instead of who the mail came from (i.e. the
#whole e-mail address). At the end of the program print out the contents of your
#dictionary.

import string
filename = "mbox-short.txt"
try:
    fhand=open(filename,"r")
except:
    print "File %s does not exist"%(filename)
    exit()

DictSenders=dict()
for line in fhand:
    if len(line)== 0: continue
    if line.startswith("From:"): continue
    if line.startswith("From"):
        words=line.split()
        sender=words[1]
        index=sender.find("@")
        domain=sender[index+1:]
       # print "debug", domain
        DictSenders[domain]=DictSenders.get(domain, 0)+1

for domain in sorted(DictSenders, key=DictSenders.get, reverse=True):
   print domain, DictSenders[domain]
   
# for Ex. 9,3for sender in sorted(DictSenders, key=DictSenders.get, reverse=True):
#    print sender, DictSenders[sender]
        
fhand.close()
