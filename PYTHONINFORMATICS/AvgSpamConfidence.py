#Reads mbox-short.txt
#finds lines starting with  X-DSPAM-Confidence: 0.8475
#Extracts the floating point number on that line
#Computes Average spam confidence

fname=raw_input("Input the file name mbox-short.txt  : ")
fd=open(fname,"r")
total=0
count=0
for line in fd:
    if len(line)!=0:
        if line.startswith("X-DSPAM-Confidence:"):
            line=line.strip()
            pos=line.find(':')
            numstr=line[pos+1: ]
            num=float(numstr.strip())
            total+=num
            count+=1
fd.close()
average=total/count
print "The Average Spam Confidence is %f"%(average)
