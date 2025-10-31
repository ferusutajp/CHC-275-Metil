# preston >

""" 

Exception handling naturally leads us to file input/output
When the program stopped running, our program is revereted back to it's initial condition
Natural way to circumvent this is to include file input/output into our program

Escape Sequences:
Special characters we put inside our strings in order to format it a certain way
    - \n = new line
These escape sequences are how filess determine when one line starts and the next one ends
You caanm really expect a \n to be implicitly placed at the end of each line

We covered exception handling for one particular reaason: 
    The file itself might not actually exist in our filesystem, and we dont want the program to stop running if the file exists


"""

# When we call the open function:
    # The contents of your file is buffered in memory
# Use close function when we are finished:
    # The buffered memory can be removed from memory, as to not take up space

file = open("names.txt", "r")
name = []
grade = []
# Variable = open("<filename">, "<mode>")
names = file.readlines()
# readlines -- takes our list of names and make each line ana item inside our list
print(names)
for i in range(len(names)):
    names[i] = names[i].strip()
print(names)
for line in file:
    line = line.strip
    line = line.split(",")
    name.append[0]
    grade.append[1]
print(name)
print(grade)
file.close