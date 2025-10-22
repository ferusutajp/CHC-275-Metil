# preston >

sizelist = []
smallsizelist = []
medsizelist = []
largesizelist = []

check = False

while check == False:
    msize = input("What is the size of the mushroom? (Or Quit) ")
    if msize.isnumeric():
        sizelist.append(msize)
        if msize < 100:
            
    elif msize == "Quit".lower():
        print(smallsizelist)
        print(medsizelist)
        print(largesizelist)
        check = True