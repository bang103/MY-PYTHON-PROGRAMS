#Searching for instances of an alphabet in a string : function find
#find(string, char, startingindex)
#Using function 'find', count the number of instances of a character in a string
#Count the number of instances of a character in a string using find function
#exercise 8.4 and exercise 8.6 combo


def findcharacter(inputstr,char,index):
        for itervar in range(index, len(inputstr)):
            if inputstr[itervar] == char:
                return itervar
        return -1

    
str=raw_input("Input the search string: ")
ch=raw_input("\n Input the character to search: ")

count=0
idx=0

while idx < len(str):
    foundit=findcharacter(str,ch,idx)
    if foundit == -1:
        break
    else:
        count+=1
        idx=foundit+1
        
if count== 0:
    print ch , " is not present in string: ", str
else:
    print "There are ", count, " instances of ", ch, " in ", str
    



