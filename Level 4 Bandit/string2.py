# preston >

newstring = "Goat1 Goat2 Goat3"
# You can split the string inot a list of elements where each element is seperated by the whitespace
# .split()
goats = newstring.split()
print(goats)

# But you can split based on parameters within strings
whack = "1101Hi1101How1101Are1101You1101"
thwack = whack.split("1101")
print(thwack)

# How about the inverse?
# .join()
space = " "
message = space.join(thwack)
print(message)
# Better way to write it // More efficient
goodmessage = " ".join(thwack)
print(goodmessage)
# Remember you can chain functions
goodermessage = " ".join(thwack).strip()
print(goodermessage)