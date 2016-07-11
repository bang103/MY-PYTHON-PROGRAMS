#Farenheight Temp=9/5*C +32
#Celcius Temp= 5/9*(F-32)

print ' Temperature Conversion \n'
print ' For Farenheight to Celius enter 1 \n'
print ' For Celius  to Farenheight enter 2 \n'


choice=raw_input()
    
if choice == '1' or choice == '2':
        tempinput = raw_input('Enter Temperature \n')
        if tempinput.isdigit():
            temp=float(tempinput)
            if choice == '1':
                tempC= 5.0/9.0*(temp-32)
                print 'Temperature in Celcius is ', tempC
            elif choice == '2':
                tempF = 9.0/5.0*temp + 32
                print 'Temperature in Farenheit is ', tempF
        else:
            print 'Temperature should be numerical value'
else:
    print 'Invalid input! enter either 1 or 2 \n'
    
