#http://www.cse.msu.edu/~cse231/PracticeOfComputingUsingPython/
#August 25, 2015

from __future__ import print_function


#appends -- to input string so both are of same length
def prepare_input(inp_string, length):
    if length>len(inp_string):     
        out_string=inp_string[:]+"-"*(length-len(inp_string))
    else: out_string=inp_string
    return out_string


#compares the 2 sequences, makes mismatches UPPERCASE,
#returns LIST of 2 sequences, matches, mismatches
def seq_compare(seq1, seq2):
    
    length=max(len(seq1),len(seq2))
    seq1=prepare_input(seq1, length)
    seq2=prepare_input(seq2, length)
        
    seq_list=list()
    tmplist1=list()
    tmplist2=list()
    index=0
    mat=0
    mismat=0
    for char in seq1:
        if char=="-" or seq2[index]=="-":
            mismat +=1
            if char.isalpha():
                tmplist1.append(char.upper())
            else:
                tmplist1.append(char)
            if seq2[index].isalpha():
                tmplist2.append(seq2[index].upper())
            else:
                tmplist2.append(seq2[index])
            
        elif char.lower() == seq2[index].lower():
            mat +=1
            tmplist1.append(char.lower())
            tmplist2.append(seq2[index].lower())
            
        elif char.lower() != seq2[index].lower():
            mismat +=1
            tmplist1.append(char.upper())
            tmplist2.append(seq2[index].upper())
            
        index +=1
        
    seq1="".join(tmplist1)
    seq2="".join(tmplist2)
    seq_list=[seq1,seq2,mat, mismat]
    return seq_list   


#Adds an indel - at the specified position
#before passing values, it has been verified that pos is >0 and <= length of seque3nce




def add_indel(seq, pos):
    seq = seq[:pos-1]+"-"+seq[pos-1:]
    return seq

    


#Deletes an indel - at the specified position
#before passing values, it has been verified that pos is >0 and within sequence index values
#if position specified contains a character other than indel, flag is set to false and unchanged sequence is returned
#if position specified contains an indel, the indel is removed and an indel added at the end of the sequence

def del_indel(seq, pos):
    tlist=list()
    if seq[pos-1]=='-':
        print(seq[:pos-1])
        print(seq[pos:])
        seq=seq[:pos-1]+seq[pos:]
        tlist.append(1)
        tlist.append(seq)
    else:
        tlist.append(0)
        tlist.append(seq)
    return tlist
  
    return tlist                              

    
##Main Program
print("This program allows you to experiment with making changes in DNA  sequences")

print("First, input the 2 DNA sequences, a series of A, T, C,G")

while True:
    inp1=raw_input("Input first DNA sequence--->   ")
    if not inp1.isalpha():
        print("Invalid Input: Only alphabets, preferably, a series of A, T, C,G")
        continue
    break

while True:
    inp2=raw_input("Input second DNA sequence--->   ")
    if not inp2.isalpha():
        print("Invalid Input: Only alphabets, preferably, a series of A, T, C,G")
        continue
    break

length_inp=max(len(inp2), len(inp1))
sequence1=prepare_input(inp1,length_inp)
sequence2=prepare_input(inp2,length_inp)


while True:
    print("(A)dd an Indel")
    print("(D)elete an Indel")
    print("(S)core the present alignment")
    print("(Q)uit")
    inp=raw_input("What would you like to do? --->  ")

    if inp.lower()=="a": #adding an indel
        
        while True:
            inp1=raw_input("Input sequence to ADD an indel (1 or 2) --->   ")
            if inp1=='1' or inp1=='2':
                break
            else:
                print("Invalid input!")
                continue
        
        while True:
            inp2=raw_input("Input the position(starting with 1) to INSERT indel --->  ")
            if not (inp2.isdigit()):
                print("Invalid input! ")
                continue
            elif inp2.isdigit():
                if inp1=='1' and (int(inp2)==0 or int(inp2)> len(sequence1)):
                    print("Invalid input! Index value should be >0 and less than sequence length")
                    continue
                elif inp1=='1' and int(inp2)<= len(sequence1):
                    pos=int(inp2)
                    sequence1=add_indel(sequence1,pos)
                    break
                if inp1=='2' and (int(inp2)==0 or int(inp2)> len(sequence2)):
                    print("Invalid input! Index value should be >0 and less than sequence length")
                    continue
                elif inp1=='2' and int(inp2)<= len(sequence2):
                    pos=int(inp2)
                    sequence2=add_indel(sequence2,pos)
                    break
        continue #finished adding an indel

    
    if inp.lower()=="d": #deleting an indel
        while True:
            inp1=raw_input("Input sequence to DELETE an indel (1 or 2) --->   ")
            if inp1=='1' or inp1=='2':
                break
            else:
                print("Invalid input!")
                continue
            
        while True:
            inp2=raw_input("Input the position(starting with 1) to DELETE indel --->  ")
            if not (inp2.isdigit()):
                print("Invalid input! ")
                continue
            elif inp2.isdigit():
                if inp1=='1' and (int(inp2)==0 or int(inp2)> len(sequence1)):
                    print("Invalid input! Index value should be >0 and <= sequence length")
                    continue
                elif inp1=='1' and int(inp2)>0 and int(inp2)<=len(sequence1):
                    pos=int(inp2)
                    tmplist=del_indel(sequence1,pos)
                    if tmplist[0]==1:
                        sequence1=tmplist[1]
                        break
                    elif tmplist[0]==0:
                        print("Invalid index: only indels i.e. '-' can be deleted")
                        break
                if inp1=='2' and (int(inp2)==0 or int(inp2)> len(sequence2)):
                    print("Invalid input! Index value should be >0 and <= sequence length")
                    continue
                elif inp1=='2' and int(inp2)>0 and int(inp2)<= len(sequence2):
                    pos=int(inp2)
                    tmplist=del_indel(sequence2,pos)
                    if tmplist[0]==1:
                        sequence2=tmplist[1]
                        break
                    elif tmplist[0]==0:
                        print("Invalid index: only indels i.e. '-' can be deleted")
                        break
        continue #finished deleting indel
    
    if inp.lower()=="s": #scoring the alignment of the two strings
        seq_list=seq_compare(sequence1, sequence2)
        sequence1=seq_list[0]
        sequence2=seq_list[1]
        matches=seq_list[2]
        mismatches=seq_list[3]
        print("     Sequence1: ", sequence1)
        print("     Sequence2: ", sequence2)

        print("     Matches      : ", matches, " in lowercase")
        print("     Mismatches   : ", mismatches, " in UPPERCASE or '-'")
        continue #finished calculating score


    if inp.lower()=="q":
        print("Bye! Thank you for using this program")
        break
    

           

