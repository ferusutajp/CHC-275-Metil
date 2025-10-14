# preston >
# aidan >
# Bank.py -- Banking System
# Sol Badguy Bank

exitcondition = False

peoplelist = ["Jack-O' Valentine", "Ashe Duran", "Hyde Kido", "Lukai Hwei", "Shinji Ikari"]
moneylist = [300000, 17, 4000, 1, -1000]

print("Welcome system administrator!")
while exitcondition == False:
    print("Which system do you want to access?")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Transfer")
    print("4. Add Account")
    print("5. Remove Account")
    print("6. List Balances")
    print("7. Quit")
    System = input("System accessed... ")
    
    # Deposit Function
    if System == "Deposit":
        print("Entering 'Despoit' system!")
        print(peoplelist)
        depositname = input("Who's account would you like to deposit money into? ")
        index = peoplelist.index(depositname)
        depositamount = input("How much money would you like to add? ")
        depositamount = int(depositamount)
        moneylist[index] = moneylist[index] + depositamount
        
    # Withdraw Function
    elif System == "Withdraw":
        print("Entering 'Withdraw' system!")
        print(peoplelist)
        withdrawname = input("Who's account would you like to withdraw money from? ")
        windex = peoplelist.index(withdrawname)
        withdrawamount = input("How much money would you like to remove? ")
        withdrawamount = int(withdrawamount)
        moneylist[windex] = moneylist[windex] - withdrawamount
            
    # Transfer Function
    elif System == "Transfer":
        print("Entering 'Transfer' system!")
        print(peoplelist)
        transfername1 = input("Who's account do you want to remove money from? ")
        tindex = peoplelist.index(transfername1)
        transferaamount = input("How much money do you want to transfer? ")
        transferaamount = int(transferaamount)
        transfername2 = input("Who's account do you want to add this money to? ")
        tindex2 = peoplelist.index(transfername2)
        moneylist[tindex] = moneylist[tindex] - transferaamount
        moneylist[tindex2] = moneylist[tindex2] + transferaamount
        
    
 
    # Add Function
    elif System == "Add Account":
        print("Entering 'Add' system!")
        addedname = input("What is the name of the user you would like to add to the system? ")
        addedvalue = input("How much money is being added to this account? ")
        addedvalue = int(addedvalue)
        peoplelist.append(addedname)
        moneylist.append(addedvalue)
        
    # Remove Function
    elif System == "Remove Account":
        print("Entering 'Remove' system!")
        print(peoplelist)
        removedname = input("What is the name of the user you would like to remove from the system? ")
        if removedname in peoplelist:
            index = peoplelist.index(removedname)
            peoplelist.pop(index)
            moneylist.pop(index)
        else:
            print("Name not processed.")

    # View Function
    elif System == "List Balances":
        print("Current account holders and balances.")
        print(peoplelist)
        print(moneylist)

    # Quit Function
    elif System == "Quit":
        print("Thank you for using our services!")
        exitcondition = True
     
    else:
        print("That is not a supported system.")