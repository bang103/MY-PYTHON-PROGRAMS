#August 18 2015
#inputs A number of the form SLAYER
#Checks whether SLAYER+SLAYER+SLAYER=layers
#Only integer operations can be used


from __future__ import print_function

def make_layers(inp):
    s=inp/100000
    layer=inp%100000
    layers=layer*10 + s
    return(layers)
        
    
print("Guess a six-digit number SLAYER so that following equation is true: ")
print("             SLAYER+SLAYER+SLAYER=LAYERS")
print("Each letter stands for the digit in the position shown")


slayer=raw_input("input a 6 digit number --->  ")
product= 3*int(slayer)
print ("SLAYER+SLAYER+SLAYER = %d" % product)
layers=make_layers(int(slayer))
print("LAYERS = %d"%layers)
if product == layers:
    print ("Good Guess! SLAYER+SLAYER+SLAYER=LAYERS")
              
