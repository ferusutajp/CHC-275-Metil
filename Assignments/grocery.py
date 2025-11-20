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

bannpr = (bannanas[1]).strip()
apppr = (apples[1]).strip()
steakpr = (bannanas[1]).strip()
milkpr = (milk[1]).strip()
ojpr = (oj[1]).strip()
eggpr = (eggs[1]).strip()
chickenpr = (chicken[1]).strip()
ricepr = (rice[1]).strip()
breadpr = (bread[1]).strip()

while check == False:
    print("------------------------------------")
    print("Items, Price($):")
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
    if option == "Add Item".lower().strip():
        print("------------------------------------")
        adoption = input("Which item would you like to add? ")
        if adoption == "Bananas".lower().strip():
        elif adoption == "Apples".lower().strip():
        elif adoption == "Steak".lower().strip():
        elif adoption == "Milk".lower().strip():
        elif adoption == "Orange Juice".lower().strip():
        elif adoption == "Eggs".lower().strip():
        elif adoption == "Chicken".lower().strip():
        elif adoption == "Rice".lower().strip:
        elif adoption == "Bread".lower().strip():
    elif option == "Remove Item".lower().strip():
        print("------------------------------------")
        reoption = input("Which item would you like to remove? ")
        if reoption == "Bananas".lower().strip():
        elif reoption == "Apples".lower().strip():
        elif reoption == "Steak".lower().strip():
        elif reoption == "Milk".lower().strip():
        elif reoption == "Orange Juice".lower().strip():
        elif reoption == "Eggs".lower().strip():
        elif reoption == "Chicken".lower().strip():
        elif reoption == "Rice".lower().strip:
        elif reoption == "Bread".lower().strip():
    #elif option == "Check Out".lower().strip():
        #