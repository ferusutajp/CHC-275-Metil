# preston >
# triangles are three sided shapes...
# three?
# like persona 3...

A1 = input("Angle one... ")
A1 = int(A1)

A2 = input("Angle two... ")
A2 = int(A2)

A3 = input("Angle three... ")
A3 = int(A3)

# v1
if (A1 == 90 and A2 + A3 == 90) or (A2 == 90 and A1 + A3 == 90) or (A3 == 90 and A1 + A2 == 90):
    print("This is a triangle! Amazing job boss.")