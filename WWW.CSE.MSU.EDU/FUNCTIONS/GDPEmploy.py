#http://www.cse.msu.edu/~cse231/PracticeOfComputingUsingPython/
#August 18, 2015
#program gave lot of errors for the unemployment file because of the trailing comma,
#on splitting string using ',' as delimiter, the last word happened to be newline because of trailing comma
#problem while calculating total

from __future__ import print_function
import string
import sys

GDP_file="gdp.txt"
UNEMP_file="unemp.csv"

print ("Input a year between 1948 and 2008 to get the average GDP and Average Unemployment")


def avg_GDP(gdp_file, year):
    #open GDP data file
    while True:
        try:
            handGDP=open(GDP_file, "r")
            break
        except:
            raw_input("Check for GDP data file \'gdp.txt\' and press any key to continue --->  ")
    total=0
     
    count=0
    avg=0
    total=0
    for line in handGDP:
        if year not in line:
            continue
        if year in line:
            words=line.split()
            total += float(words[1])
            count +=1
            
    avg = total/4
    handGDP.close()
    return (avg)
    
    
def avg_UNEMP(unemp_file, year):
    
    #open Unemployment data file
    while True:
        try:
            handUNEMP=open(UNEMP_file, "r")
            break
        except:
            raw_input("Check for Unemployment data file \'unemp.csv\' and press any key to continue --->  ")
            
    count=0
    avg=0
    total=0
    for line in handUNEMP:
        if year not in line:
            continue
        if year in line:
            line=line.rstrip()  #first remove newline
            line=line.rstrip(",")
           
            words=line.split(",")
            for word in words:
                if year in word: continue
                else:
                    count += 1
                    total += float(word)
   
    avg = total/count
    handUNEMP.close()
    
    return(avg)



#main program
#input and validate year
while True:
    while True:
        year=raw_input("Input a year between 1948 and 2008--->  ")
        if int(year)< 1948 or int(year)>2008:
            print("Invalid Year!!")
            continue
        else: break


    average_gdp=avg_GDP(GDP_file, year)
    average_unemp=avg_UNEMP(UNEMP_file, year)

    print("For year %d, the Average GDP was %0.2f and the Average Unemployment Rate was %0.2f"%(int(year), average_gdp,average_unemp))

    while True:
        yesno=raw_input("Do you want to continue Y/N ---->  ")
        if yesno.lower() == "y": break
        elif yesno.lower() == "n":
            print("Exiting program, Thank you!")
            sys.exit()
        else: continue
     
