# preston >
print("Types of fish!")
print("1. Carniviorous")
print("2. Salt Water")
print("3. Community")
fish = input("What type of fish do you want? ")
fish = str(fish)

if fish == "Carniviorous":
    print("1. Yes")
    print("2. No")
    Own = input("Do you already have a carniviorous fish? ")
    Own = str(Own)
    if Own == "Yes":
        print("They're gonna eat eachother boss??? What are you doing...")
    elif Own == "No":
        print("Alright! Enjoy your fish.")
    else:
        print("Its a yes or no question...")
elif fish == "Salt Water":
    print("Alright! Enjoy your fish.")
elif fish == "Community":
    print("Alright! Enjoy your fish. But, you should probably get more than one...")
else:
    print("Boss that's not a type of fish that we have listed...")