#Counts the number of times an alphabet appears in a strings
#Worked out example

print "This program counts the number of times an alphabet appears in a string\n"
string=raw_input("Input the string : ")
DCounter=dict()

for char in string:
    DCounter[char]=DCounter.get(char,0)+1
print DCounter
