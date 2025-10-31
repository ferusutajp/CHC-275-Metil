# preston >

"""

Project Time?
3rd Party Imports with
.import
pygame >>>
also...
matplotlib (graph)
requests (ip adress)
pybaseball (baseball)
flask (website)
tkinter (gui)

"""


# x = int(input("Enter num 1: "))
# y = int(input("Enter num 2: "))
# quotient = x/y
# print(quotient)

""" 

Runtime error = things that cause the prrogram to crash while it's running (user)
    -Zero division error
    -Value errors
    -Type error / Class error
Compile time errors = errors that don't allow the program to run (developer)
    -Indentation error
    -Missing parentheses
    -Missing colons

"""

""" 

NEW BALL KNOWLEDGE:
try:
    <code>
except <exception>:
    <if some runtime error happens, executes this block
finally:
    <regardless of if try or except succeeds, runs this codeblock>
    
We say when a program has a runtime error, the program threw an exception
exceptioin = the kind of error thaat shows up

"""


# try:
    # x = int(input("Enter num 1: "))
    # y = int(input("Enter num 2: "))
    # quotient = x/y
    # print(quotient)
# except ValueError:
    # print("Both inputs need to be numeric.")
# except ZeroDivisionError:
    # print("Denominator must be non-zero.")
    
"""  

Currently, these are only two errors being caught:
-ValueError
-ZerroDivisionError
While these are VERY helpful, there is more...
How do we catch all generic exceptions?
Exception !

"""

try:
    x = int(input("Enter num1: "))
    y = int(input("Enter num 2: "))
    quotient = x/y
    print(quotient)
except ValueError:
    print("Both inputs need to be numeric.")
except ZeroDivisionError:
    print("Denominator must be non-zero.")
except Exception as wowzers: #wowzers is the variable name, while Exception is the required class
    print(wowzers)
finally:
    print("Wow!!!")

# Finally blocks are not required, but if you are using a Try block, atleast one Except block is required

