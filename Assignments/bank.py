# preston >
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
    if System == "Deposit" or "deposit":
        print("Entering 'Despoit' system!")
        print(peoplelist)
        depositname = input("Who's account would you like to deposit money into?")
        if depositname == "Jack-O' Valentine":
            print("lalalalalala")

    # Quit Function
    if System == "Quit":
        print("Thank you for using our services!")
        exitcondition = True