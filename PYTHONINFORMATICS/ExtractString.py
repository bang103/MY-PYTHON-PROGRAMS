
#Exercise 6.5 Take the following Python code that stores a string:
#str = 'X-DSPAM-Confidence: 0.8475'
#Use find and string slicing to extract the portion of the string after the colon
#character and then use the float function to convert the extracted string into a
#floating point number.

print 'Extracting floating point number from the follwing string and printing it out'
print 'X-DSPAM-Confidence: 0.8475'

str = 'X-DSPAM-Confidence: 0.8475'
colonpos= str.find(':')
print 'position of colon', colonpos
print 'see..found the colon!', str[colonpos]
substr = str[colonpos+1:]
substr.strip()
number=float(substr)
print number
print type(number)
