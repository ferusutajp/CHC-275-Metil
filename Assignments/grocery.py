# preston >

print("Welcome to the grocery store system!")
check = False

itemdoc = open("foods.txt", "r")
items = itemdoc.readlines()

bannanas = (items[0]).strip().split(",")
apples = (items[1]).strip().split(",")
steak = (items[2]).strip().split(",")
milk = (items[3]).strip().split(",")
oj = (items[4]).strip().split(",")
eggs = (items[5]).strip().split(",")
chicken = (items[6]).strip().split(",")
rice = (items[7]).strip().split(",")
bread = (items[8]).strip().split(",")

bannp = (bannanas[1]).strip()
print(bannp)
x = input("lalalla")

while check == False:
    print("------------------------------------")
    print("Items:")
    print(bannanas)
    print(apples)
    print(steak)
    print(milk)
    print(oj)
    print(eggs)
    print(chicken)
    print(rice)
    print(bread)
    print("------------------------------------")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Check Out")
    option = input("Which function do you want to select? ").strip().lower()
    #if option == "Add Item".lower().strip():
        #
    #elif option == "Remove Item".lower().strip():
        #
    #elif option == "Check Out".lower().strip():
        #