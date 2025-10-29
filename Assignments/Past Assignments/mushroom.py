# preston >
# teague >

sizelist = []
smallsizelist = []
medsizelist = []
largesizelist = []

check = False

while check == False:
    msize = input("What is the size of the mushroom? (Or Quit) ")
    if msize.isnumeric():
        msize = int(msize)
        sizelist.append(msize)
        if msize < 100:
            smallsizelist.append(msize)
        elif msize >= 100 and msize <= 200:
            medsizelist.append(msize)
        elif msize > 200:
            largesizelist.append(msize)
    elif msize == "Quit".lower():
        print(f"Small sizes: {smallsizelist}")
        print(f"Medium sizes: {medsizelist}")
        print(f"Large sizes: {largesizelist}")
        check = True