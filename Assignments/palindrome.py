# preston >
# teague >

word = input("Enter your word: ")
palidrome = False
print(f"Your word is: {word}")

inverse = word[::-1]

if inverse.strip().lower() == word.strip().lower():
    palidrome = True

if palidrome == True:
    print(f"{word} is a palidrome!")
elif palidrome == False:
    print(f"{word} is not a palidrome!")