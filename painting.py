room = [['length','height','width','radius','circumference',"room's","object's"],[0,0,0,0],[0,0,0,0]]
amount = [0]

def Objects(amount2):
    amount = amount2
    error = "no"
    while error == "no":
        try:
            quantity = float(input("How many objects of this type are there? "))
            error = "yes"
        except ValueError:
            print("Error!Float only!")

        amount2*=quantity
    
        room[2][3] += amount2
        room[2][3] -= amount
        if room[2][3] > room[1][3]:
            print("Size of unpainted objects is larger then room. Objects rejected")
            room[2][3] -= amount2


def Calculate (value,value2,a,y):
    room[y][3]+= value*value2*a
    amount[0] = value*value2*a

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

finalUnpainted = 0
CalculateRegular(3,5,1)
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
        amount2 = radius*radius*3.1415
        Objects(amount2)
    else:
        CalculateRegular(2,6,2)
        Objects(amount[0])
    answer = input("Another object? Use Y/N")

totalArea = room[1][3] - room[2][3]
print("final values of both")
print(room[1][3])
print(room[2][3])
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
print("You will need ",gallons, "gallons of paint.")
