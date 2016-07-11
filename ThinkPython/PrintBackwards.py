#input a string and print it backwards

input=raw_input(" Input a string to print backwards: ")

for index in range (-1, -(len(input)+1), -1):
    print input[index], "\n"
    
