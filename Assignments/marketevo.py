# preston >

day1 = open("day1_20.txt", "r")
buffer1 = day1.readlines()
day1.close()

day2 = open("day21_40.txt", "r")
buffer2 = day2.readlines()
day2.close()

msft = (buffer1[0]).strip().split(",").pop(0)

amzn = (buffer1[1]).strip().split(",").pop(0)
nvda = (buffer1[2]).strip().split(",").pop(0)

msft2 = (buffer2[0]).strip().split(",")
amzn2 = (buffer2[1]).strip().split(",")
nvda = (buffer2[2]).strip().split(",")