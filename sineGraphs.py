import math
option = input("Will you enter the angle or sine? Use A/S")
def Angles():
    angle = int(input("Enter your angle in degrees"))
    angleRad = math.radians(angle)
    math.sin(angleRad)
    maximum = int(input("What is the largest value of x you will be looking at?"))
    maximum = (maximum//360)*360
    print(maximum)
    minimum = int(input("What is the smallest value of x you will be looking at?"))
    if minimum%360 != 0:
        minimum = minimum/360
        minimum += 1
        minimum = minimum//1
    minimum *= 360
    print(360)

Angles()
    
    
