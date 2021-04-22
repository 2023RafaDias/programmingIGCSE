import math
angles=[]
quantity = 0
count = 0
enter = [1]
def angleSine():
    error = "no"
    while error == "no":
        option = input("Will you enter the angle or sine? Use A/S")
        if option == "A":
            okay = "yes"
            while okay == "yes":
                try:
                    angle = float(input("Enter your angle in degrees: "))
                    okay = "no"
                except ValueError:
                    print("Invalid! Please use a real number")
            error = "Y"
        elif option =="S":
            okay2 = "yes"
            while okay2 == "yes":
                okay = "yes"
                while okay == "yes":
                    try:
                        sine = float(input("Enter the sine: "))
                        okay = "no"
                    except ValueError:
                        print("Invalid! Please use a real number")
                if sine < -1 or sine > 1:
                    print("Invalid Sine! Should be between 1 and -1")
                else:
                    okay2 = "no"
            angle = math.asin(sine)
            angle = math.degrees(angle)
            error = "Y"
        else:
            print("INVALID! Please use A or S")
            enter[0] = 0
    return angle
              
def Find(quantity, angle):
    count = 0
    error = "yes"
    while error == "yes":
        try:
            maximum = float(input("What is the largest value of x you will be looking at?"))
            error = "no"
        except ValueError:
            print("INVALID! Must Use a Real Number!")

    while error == "no":
        try:
            minimum = float(input("What is the smallest value of x you will be looking at?"))
            error = "yes"
        except ValueError:
            print("INVALID! Must Use a Real Number!")
            
    value = minimum/180
    if minimum%180 != 0:
        minimum = minimum/180
        minimum += 1
        value = minimum//1
    value *= 180
    while value <= maximum:
        addSubtract = value%360
        if addSubtract == 0:
            angles.append(value+angle)
            count+= 1
            quantity+=1
        else:
            angles.append(value-angle)
            count+=1
            quantity += 1
        value +=180
    print("The angles with the same sine as ", angle, " between this range will be: ")
    for i in range (quantity-count, len(angles)):
        if angles[i]>= minimum and angles[i]<=maximum:
            print(angles[i])

error = "Y"
while error == "Y":
    Find(quantity,angleSine())
    error = input("Would you like to go again?")
    
    
#find the smalles multiple of 180 inside the range!!!!!!!! Then, calculate all values of angle until x > maximum... and done
