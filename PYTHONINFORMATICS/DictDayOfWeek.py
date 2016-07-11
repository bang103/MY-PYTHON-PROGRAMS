#Exercise 9.2 in Python for INformatics
#Exercise 9.2 Write a program that categorizes each mail message by which day of
#the week the commit was done. To do this look for lines which start with *From*,
#then look for the third word and then keep a running count of each of the days
#of the week. At the end of the program print out the contents of your dictionary
#(order does not matter).


import string
filename = "mbox-short.txt"

try:
    fhand=open(filename,"r")
except:
    print "File %s does not exist"%(filename)
    exit()

DaysOfWeek=dict()
for line in fhand:
    if len(line)== 0: continue
    if line.startswith("From:"): continue
    if line.startswith("From"):
        words=line.split()
        day=words[2]
        DaysOfWeek[day]= DaysOfWeek.get(day,0)+1
for day in DaysOfWeek:
    print day, DaysOfWeek[day]
fhand.close()
