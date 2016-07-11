#August 11, 2015
#http://www.cse.msu.edu/~cse231/PracticeOfComputingUsingPython/

from __future__ import print_function


#staring point for vending machine
vend_nickels=25
vend_dimes=25
vend_quarters=25
vend_ones=0
vend_fives=0


#print available balance with vending machine
def print_vend_balance():
    print('Vending machine stock:')
    print("     %d nickels"%vend_nickels)
    print("     %d dimes"%vend_dimes)
    print("     %d quarters"%vend_quarters)
    print("     %d ones"%vend_ones)
    print("     %d fives"%vend_fives)


def print_deposit_menu():
    print('Menu for deposits:')
    print('     n - deposit a nickel')
    print('     d - deposit a dime')
    print('     q - deposit a quarter')
    print('     o - deposit a one dollar bill')
    print('     f - deposit a five dollar bill')
    print('     c - cancel the purchase)')


def calc_change(balance):
    global vend_nickels
    global vend_dimes
    global vend_quarters
    
    print("Your change: ")
    if vend_quarters > 0 and balance>0:             
        req_quarters=balance/25
        if req_quarters <= vend_quarters:  
            vend_quarters -=req_quarters
            change_quarters=req_quarters
            balance -= change_quarters*25
        else:
            change_quarters=vend_quarters
            vend_quarters=0
            balance -= change_quarters*25
        print ("    %d quarters"%change_quarters)
        
    if vend_dimes > 0 and balance > 0:                
        req_dimes=balance/10
        if req_dimes <= vend_dimes:  
            vend_dimes -=req_dimes
            change_dimes=req_dimes
            balance -= change_dimes*10
        else:
            change_dimes=vend_dimes
            vend_dimes=0
            balance -= change_dimes*10
        print ("    %d dimes "%change_dimes)

    if vend_nickels > 0 and balance>0:          
        req_nickels=balance/5
        if req_nickels <= vend_nickels:  
            vend_nickels -=req_nickels
            change_nickels=req_nickels
            balance -= change_nickels*5
        else:
            change_nickels=vend_nickels
            vend_nickels=0
            balance -= change_nickels*5
        print ("    %d nickels"%change_nickels)
    
   
    if balance > 0:
        print("Machine has insufficient change(coins).")
        print("Please contact front desk to collect $%.2f"%(float(balance)/100.0))
        print_vend_balance()
        
    else: print_vend_balance()
      
            
    
  
 #main program   
print("Welcome to the vending machine change maker program!")
print("Change maker initialized.")
print_vend_balance()

while True:
    print ("The purchase price of all items is in multiples of 5")
    inp=raw_input("Input the purchase price xx.xx or 'q'/'Q' to Quit---> ")
    if inp.lower()=="q":            #quit program
        print("Bye, ending program")
        print_vend_balance()
        break
    else:       
        try:                        #check for valid numeric input
            purchase_price=float(inp)
        except:
            print("Invalid input!! Purchase price must be a numeric value")
            continue
        
        purchase_price=int(purchase_price*100)  # %operator needs integer operand
        if purchase_price % 5 != 0:             #check for divisibility by 5
            print("Invalid input!! Purchase price must be divisible by 5")
            continue
        else:                                    #main program
            cancelled=False
            amount_paid=0
            amount_payable=purchase_price
            print_deposit_menu()
            #Keep accepting currency till purchase price equalled/exceeded or transaction cancelled
            while True: 
                print ("Amount payable by you--->  ", float(amount_payable)/100.00)
                denom=raw_input("Enter currency denomination--->  ")
                
                if denom.lower()=="n":
                    amount_paid +=5
                    vend_nickels +=1
                elif denom.lower()=="d":
                    amount_paid +=10
                    vend_dimes +=1
                elif denom.lower()=="q":
                    amount_paid +=25
                    vend_quarters +=1
                elif denom.lower()=="o":
                    amount_paid +=100
                    vend_ones +=1
                elif denom.lower()=="f":
                    amount_paid +=500
                    vend_fives +=1
                elif denom.lower()== "c":
                    cancelled=True
                    break
                else:
                    print("Invalid Input: refer to menu")
                    continue
                if amount_paid<purchase_price:
                    amount_payable=purchase_price - amount_paid
                else: break
                
            if cancelled==True:
                change_from_machine=amount_paid
            else:
                change_from_machine=amount_paid - purchase_price

            #return correct amount of change with minimum coins
            if change_from_machine== 0:
                print("No change due")
            else:
                calc_change(change_from_machine)
            
            

