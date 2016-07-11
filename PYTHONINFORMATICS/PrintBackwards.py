#Exercise 6.1 Write a while loop that starts at the last character in the string and
#works its way backwards to the first character in the string, printing each letter on
#a separate line, except backwards.

print 'Program inputs a string and prints it backwards'
print 'Each character on a separate line'

inputstring = raw_input('Enter a string to print backwards \n')

print 'length of string', len(inputstring)
print 'Backwards'
for index in range(-1,-(len(inputstring)+1) ,-1):
    print inputstring[index], '\n'

print 'Forwards'
for index in range(len(inputstring)):
    print inputstring[index], '\n'
