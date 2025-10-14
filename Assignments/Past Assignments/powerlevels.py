# preston >
num1 = input("Input your first number! ")
num2 = input("Input your second number! ")
num1 = int(num1)
num2 = int(num2)

if num1 == num2:
    print(f"{num1} and {num2} are equal!")
elif num1 > num2:
    print(f"{num1} is greater than {num2}!")
elif num1 < num2:
    print(f"{num1} is less than {num2}!")
else:
    print("idk what you did boss???")