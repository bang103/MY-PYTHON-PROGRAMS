#From Make way for the ducklings
#print Jack, Kack, Lack, Mack, Nack,
#Ouack, Pack, and Quack.

prefixes ="JKLMNOPQ"
suffix = "ack"
for char in prefixes:
    if char == 'O'or char == 'Q':
        print char+'u'+suffix
    else:
        print char+suffix
