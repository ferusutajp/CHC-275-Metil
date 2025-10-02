# preston >
# Bank.py -- Banking System

exitcondition = False

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
    
    
    # Quit Function
    if System == "Quit":
        print("Thank you for using our services!")
        exitcondition = True