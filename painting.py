room = [['length','height','width','radius','circumference',"room's","object's"],[0,0,0,0],[0,0,0,0]]

def Objects():
    amount = 0
    quantity = 0
    error = "yes"
    while error == "yes":
        try:
            quantity = int(input("How many objects of this type are there?"))
            error = "no"
        except ValueError:
            print("Float Only!")
    amount= room[2][3]
    for i in range(1,quantity):
        room[2][3]+= amount
    amount = amount*quantity
    if room[2][3]> room[1][3]:
        
        print("Area unpainted is larger than area painted. INVALID objects")
        room[2][3]-= amount

def Calculate (value,value2,a,y):
    room[y][3]+= value*value2*a
    amount = value*value2*a

def CalculateRegular (x,z,y):
    for i in range (0,x):
        error = "yes"
        while error == "yes":
            print("please enter the ",room[0][z],room[0][i])
            try:
                room[y][i]=float(input())
                error = "no"
            except ValueError:
                print("Float Only!")

    m = 0
    for i in range (0,x-1):
        Calculate(room[y][m],room[y][1],x-1,y)
        m = 2

CalculateRegular(3,5,1)
print(room[1][3])
answer = input("Are there any unpaintable objects? Use Y/N")
while answer == "Y":
    shape = ""
    while shape != "Y" and shape != "N":
        shape = input("Is your shape circular? Use Y/N")
    if shape == "Y":
        error = "no"
        while error == "no":
            try:
                radius = float(input("Please enter the shape's radius: "))
                error = "yes"
            except ValueError:
                print("Float Only!")

        room[2][3]+= radius*radius*3.1415
        amount = radius*radius*3.1415
        Objects()
    else:
        CalculateRegular(2,6,2)
        Objects()
    answer = input("Another object? Use Y/N")

totalArea = room[1][3] - room[2][3]
print(totalArea)

error = "yes"
while error == "yes":
    try:
        multiply = float(input("How Many coats of paint?"))
        error = "no"
    except ValueError:
        print("Invalid Entry! Float only!")

totalArea *= multiply
gallons = totalArea/400
print("You will need, ",gallons, "gallons.")

#LABEL OBJECTS!
#STORE OBJECTS THAT WERE INVALIDATED. 
