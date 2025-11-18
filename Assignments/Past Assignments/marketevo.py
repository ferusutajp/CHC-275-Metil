# preston >

day1 = open("day1_20.txt", "r")
buffer1 = day1.readlines()
day1.close()

day2 = open("day21_40.txt", "r")
buffer2 = day2.readlines()
day2.close()

msft = (buffer1[0]).strip().split(",")
msft.pop(0)
amzn = (buffer1[1]).strip().split(",")
amzn.pop(0)
nvda = (buffer1[2]).strip().split(",")
nvda.pop(0)

for i in range(len(msft)):
    msft[i] = int(msft[i])
    amzn[i] = int(amzn[i])
    nvda[i] = int(nvda[i])

msft2 = (buffer2[0]).strip().split(",")
msft2.pop(0)
amzn2 = (buffer2[1]).strip().split(",")
amzn2.pop(0)
nvda2 = (buffer2[2]).strip().split(",")
nvda2.pop(0)

for i in range(len(msft2)):
    msft2[i] = int(msft2[i])
    amzn2[i] = int(amzn2[i])
    nvda2[i] = int(nvda2[i])

msftmean = (sum(msft)) / len(msft)
amznmean = (sum(amzn)) / len(amzn)
nvdamean = (sum(nvda)) / len(nvda)
msft2mean = (sum(msft2)) / len(msft2)
amzn2mean = (sum(amzn2)) / len(amzn2)
nvda2mean = (sum(nvda2)) / len(nvda2)

file = open("marketevo_results.txt", "w")
file.write("Stock market report for Microsoft (MSFT), Amazon (AMZN), and Nvidia (NVDA):\n")
file.write("\n")
file.write("Day 1-20 Averages:\n")
file.write(f"MSFT average: {msftmean}\n")
file.write(f"AMZN average: {amznmean}\n")
file.write(f"NVDA average: {nvdamean}\n")
file.write("\n")
file.write("Day 21-40 Averages:\n")
file.write(f"MSFT average: {msft2mean}\n")
file.write(f"AMZN average: {amzn2mean}\n")
file.write(f"NVDA average: {nvda2mean}\n")
file.write("\n")
if (msft2mean > msftmean):
    file.write("MSFT is trending upwards, purchase reccommended.\n")
if (amzn2mean > amznmean):
    file.write("AMZN is trending upwards, purchase reccommended.\n")
if (nvda2mean > nvdamean):
    file.write("NVDA is trending upwards, purchase reccommended.\n")
file.write("\n")
file.write("Conclusion of report.")
file.close()