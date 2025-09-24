# preston >

# Defining x
x = input("Enter your number. ")
x = int(x)

# Math Process
while x != 1:
<<<<<<< HEAD
    print(x)
    if x % 2 == 0:
        x = x / 2
    elif x % 2 == 1:
        x = 3 * x + 1
if x == 1:
    print(x)
=======
    while x % 2:
        x = x / 2
        print(x)
    else:
        x = x + 1
        print(x)
>>>>>>> aa144e3bb329b5f52d25280fefcdfce320f4c397
