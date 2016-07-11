#Read a file and convert all to caps

filename = raw_input("For which file do you want to change the volume? ")
try:
    fd = open(filename, "r")
except:
    print "%s does not exist " % (filename)
    exit
    
filename2 = raw_input("Enter name of output file to store SHOUTED text  ")
fd2= open(filename2, "w")

for line in fd:
    if len(line) != 0:
        fd2.write(line.upper())

fd.close()
fd2.close()

    
