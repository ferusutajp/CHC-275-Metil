# preston >

check = True

while check == True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")
    Function = str(input("Which function do you want to access?"))
    if Function.lower() == "Addition":
        try:
            x = int(input("Enter first number: "))
            y = int(input("Enter second number: "))
            ResultAdd = x + y
            print(ResultAdd)
        
    elif Function.lower() == "Subtraction":
    elif Function.lower() == "Multiplication":
    elif Function.lower() == "Division":