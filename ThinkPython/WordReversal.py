#inputs 2 strings and compares them to see if they are palindromes



def palindrome(string1, string2):
    if len(string1) != len(string2):
        return False
    else:
        reverse = string2[::-1]
        if string1==reverse:
            return True
        else:
            return False
        #increasing index for string1, decreasing index for string2-works fine
#        itr2=-1
#        for itr1 in range(0, len(string1) - 1):
#            if string1[itr1] != string2[itr2]:
#                return False
#            else:
#                itr2-=1
#    return True

##****should redo using lists    
#        #reverse string2
#        reverse = ""
#        for itervar in range (-1, -(len(string2)+1), -1):
#            reverse=reverse+string2[itervar]
#        if string1==reverse:
#            return True
#        else:
#            return False
    
str1=raw_input("Input the first string : ")
str2=raw_input("\n Input the second string : ")
result = palindrome(str1, str2)
if result:
    print str1, " and " ,str2, " are  palindromes"
else:
    print str1, " and " ,str2, " are not palindromes"

    
