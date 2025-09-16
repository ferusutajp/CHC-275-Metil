# preston >
# love the super seniors

# freshie = $5
# soph chud = $7
# junior slop = $9
# senior = $11
# super senior = $15 + freshmen

print("Welcome to the lunch loan system!")
print("Enter your grade level!")
print("1. You are a Freshman. ")
print("2. You are a Sophomore. ")
print("3. You are a Junior. ")
print("4. You are a Senior. ")

Grade = input("Input your grade level! ")

if Grade == "Freshman":
    print(f"You are a {Grade}! You get $5 for lunch, you peasant. ")
elif Grade == "Sophomore":
    print(f"You are a {Grade}! You get $7 for lunch, try to buy anything geek... ")
elif Grade == "Junior":
    print(f"You are a {Grade}! You get $9 for lunch, go wait in that sandwhich line for 35 minutes! ")
elif Grade == "Senior":
    print(f"You are a {Grade}! You get $11 for lunch!")
elif Grade == "Super Senior":
    print(f"You are a {Grade}! I know what you are... But you get $15 for lunch :D ")
else:
    print("Thats not a grade level... Bum... ")