# preston >

# Defining x
x = input("Enter your number. ")
x = int(x)

# Math Process
while x != 1:
    print(x)
    if x % 2 == 0:
        x = x / 2
    elif x % 2 == 1:
        x = 3 * x + 1

if x == 1:
    print(x)