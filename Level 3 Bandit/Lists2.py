# preston >

list = [10, 20, 30, 40, 50]
# indicies [0, 1, 2, 3, 4]

""" 
range(<listname>) creates list of numbers corresponding to the indices of a list
range(len(<listname>)) = [0, 1, 2, 3, 4]
"""

for i in range(len(list)):
    print(list[i])
    
for num in list:
    print(num)
    
while i < len(list):
    print(list[i])
    i = i + 1
    
""" 
1. For-i Loop
2. For-each Loop
3. While Loop
"""

""" 
You can add / remove 'things' to lists
Add: (Apppend)
<listname>.append(<added value>)
Remove:
<listname>.remove(<removed value>)
<listname>.pop(<removed index>)
"""

Gurtlist = ["One", "Two"]
print(Gurtlist)
Gurtlist.append("Three")
print(Gurtlist)
Gurtlist.remove("One")
print(Gurtlist)
Gurtlist.pop(0)
print(Gurtlist)

"""
Checker = []
check = False
while check == False:
    Checker = input("Input... ")
    if Checker == "Quit":
        check = True
    else:
        Checker.append(Checker)
        print(Checker)
"""
        
StudentList = ["Ky", "Sol", "Ramlethal", "Romeo"]
GpaList = [94, 82,  12, 101]

for i in range(len(StudentList)):
    print(f"Student: {StudentList[i]} - GPA: {GpaList[i]}")
    
# .index :DDDD
# <listname>.index(<value>) returns the index of the object in our list

index = StudentList.index("Sol")
print(index)