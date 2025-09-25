# preston >

# <list name> = [<attributes>]

list = [5, 10, 15, 20]
print(list)

# index = the numerical pos. of thje obj. within the list
# syntax = print(list[index])

print(list[0])

"""
indexprint = input(":p ")
indexprint = int(indexprint)
if indexprint <= 3:
    print(list[indexprint])
"""
    
# iterator = a number that corressponds to the current index that you're trying to access
# typically, i denotes your iterator

i = 0 # the current index is the first one // set it to zero
i = int(i)

while i <= 3:
    print(list[i])
    i = i + 1
    
# for <placeholder name> in <list name>:
#   <script>

newlist = [2, 4, 6, 8]
print("with forloop")
for num in newlist:
    print(num)
    
for num2 in newlist:
    num = num + 5
    
x = 0
while x <= 3:
    newlist[x] = newlist[x] + 5
    x = x + 1
    
print(newlist)

# for loops create copies of lists
# while loops directly access lists

# len = length of a list
print(len(newlist), "'things' in the list; newlist.")