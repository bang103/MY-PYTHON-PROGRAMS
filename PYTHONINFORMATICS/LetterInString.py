#program counts the number of times the letter a appears in a string:
#Encapsulate this code in a function named count, and generalize it
#so that it accepts the string and the letter as arguments.

def countstr(str, substr):
    lowstr = str.lower()
    lowsubstr=substr.lower()
    count = lowstr.count(lowsubstr)
    return count

print 'Prints out the occurence of a substring (case independent) in a given string'
str=raw_input('Input the string on which you will perform a search')
substr= raw_input('What is it that you want to search for ?')
print substr, ' occurs ', countstr(str, substr), '  times in  ' , str
                
