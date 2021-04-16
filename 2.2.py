miles = []
gallons = 0
distance = 0
need = []
amount = 0
count = -1
more = "yes"
correct = ""
while more == "yes":
    while correct != "yes":
        try:
            miles.append(float(input("Enter the mileage of the car the last time it was filled: ")))
        except ValueError:
            print("integer only!")

        try:
            miles.append(float(input("Enter the mileage of the car now that the tank is empty: ")))
        except ValueError:
            print("integer only!")
        
        distance = miles[count+2] - miles[count+1]
        if distance < 1:
            miles.pop(count+2)
            miles.pop(count+1)
            print("Invalid options as the amount of miles can't have decreased. Verify for error in your car's system")
        else:
            correct = "yes"
    try:
        litres = float(input("Litres to fill the tank: "))
    except ValueError:
        print("integer only!")

    gallons = litres*0.26
    need.append(gallons/distance)
    print("The amount of gallons this car needs of is ", need[amount])
    amount += 1
    count+=2
    correct = ""
    more = input("Is there another car you would like to verify?")
for i in range (0,amount):
    print("Car ",i+1," requires ",need[i]," gallons.")

