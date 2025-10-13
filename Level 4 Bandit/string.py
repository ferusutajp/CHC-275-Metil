# preston >

# Essentially, strings are lists

hellostring = "hello"
for character in hellostring:
    print(character)
    
# Lists and strings both inherit from the same parent which is called an iterable

""" 
.strip() // Removes leading and trailing whitespace
.upper() // Forces uppercase
.lower() // Forces lowercase
"""

peak = "A"
print(peak)
peak = peak.lower()
print(peak)

option = input("Enter number... ")
if option.isnumeric():
    option = int(option)
    option = option + 5
    print(option)
else:
    print("lalalalala")

""" 
.isnumeric() // Returns True if the strings its called on is a number
"""

lala = "Gulp Gulp Gulp \nGulp Gulp \nGulp!"
print(lala)

""" 
.splitlines() // Returns a list of strings where each element is split by a newline
"""