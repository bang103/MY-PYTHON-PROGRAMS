#http://www.cse.msu.edu/~cse231/PracticeOfComputingUsingPython/
#August 13, 2015
#Under programs using functions
#took 3 hours just to write in python and debug!


from __future__ import print_function
import random

#function to shuffle the string passed to it, using random.shuffle(list)
#returns a string
def shuffle_word(ipstring):
    tmplist=list(ipstring)
    random.shuffle(tmplist)
    shuffstring="".join(tmplist)
    
    return shuffstring



#function to trim punctuation as well as first and last alphabet of a word
#first_part: collect characters till you reach an alphabet
#=>punctuation marks and first alphabet of word are collected
#last_part: last part=collect characters till you reach an alphabet
#=>punctuation marks and last alphabet of word are collected
#returns a list : lstword=[first_part,middle_part,last_part]

def trim_word(ipstring):
                                       #carve out first part of word
    idx1=0
    first_part=list()
    while not ipstring[idx1].isalpha():
        first_part.append(ipstring[idx1])
        idx1 +=1
    first_part.append(ipstring[idx1]) #also append first alphabet after punctuations
    first_part="".join(first_part)
                                      #carve out last part of word

    idx2=len(ipstring)-1
    last_part=list()
    while not ipstring[idx2].isalpha():
        last_part.append(ipstring[idx2])
        idx2 -=1
    last_part.append(ipstring[idx2])  #also append last alphabet after punctuations
    last_part="".join(last_part)
    last_part=last_part[::-1]
        

    middle_part =ipstring[idx1+1:idx2]
    lstword=[first_part,middle_part,last_part]
    
        
    lstword=[first_part,middle_part,last_part]

   
    return lstword
        

#main program

#first open the inputfile
while True:
    try:
        fhandinput=open("ScrambledWordsIp.txt")
        break
    except:
        raw_input("Locate input file ScrambledWordsIp.txt, then press any key to continue")
        continue       


#create an outputfile to output scrambled text
fhandoutput=open("ScrambledOutput.txt", "w")


for line in fhandinput:                     #for each line in file
    words_in_line=line.split()              #create list of words in file

    
    list_output_line=list()
    for each_word in words_in_line:
                                    #trim only words which have length more than 3                                
        if len(each_word)> 3:
            lst_trimmed_word=trim_word(each_word)
                                    #if word contains a hyphen or a '
            if ("-" in lst_trimmed_word[1]) or ("'" in lst_trimmed_word[1]):
                if ("-" in lst_trimmed_word[1]):
                                        #split into two sub-words at the hyphen or '
                    tmplist=lst_trimmed_word[1].split("-")
                elif ("'" in lst_trimmed_word[1]):
                    tmplist=lst_trimmed_word[1].split("'")

                                        #now shuffle the words separated by hyphen/'
                #if len(tmplist[0])> 3:
                    #sublist1=trim_word(tmplist[0])
                    #tmpstr1=shuffle_word(sublist1[1])
                    #subword1=sublist1[0]+tmpstr1+sublist1[2]
                #elif len(tmplist[0])<= 3:
                subword1=shuffle_word(tmplist[0])
                    
                    
                #if len(tmplist[1])> 3:
                    #sublist2=trim_word(tmplist[1])
                    #tmpstr2=shuffle_word(sublist2[1])
                    #subword2=sublist2[0]+tmpstr2+sublist2[2]
                #elif len(tmplist[1])<= 3:
                subword2=shuffle_word(tmplist[1])
                      
                if ("-" in lst_trimmed_word[1]):
                    shuffled_word=lst_trimmed_word[0]+ subword1 + "-"+subword2+lst_trimmed_word[2]
                elif ("'" in lst_trimmed_word[1]):
                    shuffled_word=lst_trimmed_word[0]+ subword1 + "'"+subword2+lst_trimmed_word[2]
                
              
                                    #word does not contain hyphen or apostrophe
            else:
                tmpstring=shuffle_word(lst_trimmed_word[1])
                shuffled_word=lst_trimmed_word[0]+tmpstring+lst_trimmed_word[2]
                
                
                                    #append shuffled word to output list

        elif len(each_word)<=3:
            shuffled_word=each_word

        list_output_line.append(shuffled_word)
            

    str_output_line= " ".join(list_output_line)
    
    fhandoutput.write(str_output_line)
    
fhandinput.close()
fhandoutput.close()


            

            
            
        
