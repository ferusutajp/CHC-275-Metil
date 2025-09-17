# preston >

"""
Loop Types: (Easy to hard...)
-While Loops
-For Loops
-Recursion 
"""

"""
Syntax:
while <exit condition>
    <repeated action>
    
Exit Condition is a boolean
Will constantly check for exit condition
    Compete action
    Check for condition
    If condition not met
    Repeat
"""

x = 1
while x <= 10:
    print(x)
    x = x + 1

nums = [1,2,3,4,5,6,7,8,9,10]

check = False

while check == False:
    print("Option One")
    print("Option Two")
    print("Option Three")
    option = input("Select your option. ")
    if option == "Quit":
        check = True
    elif option == "One":
        print("noob")