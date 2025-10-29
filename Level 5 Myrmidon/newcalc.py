# preston >

check = True

while check == True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")
    Function = str(input("Which function do you want to access? "))
    if Function.lower() == "addition":
        try:
            xa = int(input("Enter first number: "))
            ya = int(input("Enter second number: "))
            ResultAdd = xa + ya
            print(ResultAdd)
        except ValueError:
            print("ValueError -- Please input numeric values")
    elif Function.lower() == "subtraction":
        try:
            xs = int(input("Enter first number: "))
            ys = int(input("Enter second number: "))
            ResultSub = xs - ys
            print(ResultSub)
        except ValueError:
            print("ValueError -- Please input numeric values")
    elif Function.lower() == "multiplication":
        try:
            xm = int(input("Enter first number: "))
            ym = int(input("Enter second number: "))
            ResultMul = xm * ym
            print(ResultMul)
        except ValueError:
            print("ValueError -- Please input numeric values")
    elif Function.lower() == "division":
        try:
            xd = int(input("Enter first number: "))
            yd = int(input("Enter second number: "))
            ResultDiv = xd / yd
            print(ResultDiv)
        except ValueError:
            print("ValueError -- Please input numeric values")
        except ZeroDivisionError:
            print("ZeroDivisionError -- Cannot divide by zero")
    elif Function.lower() == "quit":
        check = False
        print("Calculator closed")
    else:
        print("Invalid input -- Please select a valid function or quit")