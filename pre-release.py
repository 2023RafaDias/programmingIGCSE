import random

courts = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]

corresponding = ["code","name","phone"]
names = ["Hour","Court"]
guests = []

hours = [8,9,10,11,12,13,14,15,16,17,18]

amount = [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]
most = [0,0]

totalNumber = 0

day = "started"
print("Day Has Started")
print(" ")

def timeArray(selected):
    for i in range(0,10):
        if selected == hours[i]:
            return int(i)

def Availability(i,j):
    if not(courts[i][j]):
        print("Free")
    else:
        print("booked")
        position = courts[i][j]-1
        for i in range(0,3):
            print(corresponding[i],": ",guests[position][i])

def Schedule(court,time):
    guests.append([])                          
    guests[-1].append(1890)

    rep = len(guests)
    if rep > 1:
        for i in range(0,rep-1):    
            while guests[-1][0] == guests[i][0]:
                guests[-1][0] = random.randint(1000,9999)
    
    name = input("What is the guest's name?")
    guests[-1].append(name)
    correct = "NO"
    while correct != "Y":
        phone = input("Enter the guest's phone number: ")
        print(phone)
        correct = input("Does the user confirm the number?")
    guests[-1].append(phone)
    courts[court][time] = len(guests)

def CourtSchedule():
    timeOption = int(input("At what time would you like to book?"))
    time = timeArray(timeOption)
    count = 0
    enter = 0
    while enter == 0:
        for i in range(0,8):
            if not(courts[i][time]):
                print("Court ",i+1,": free")
                enter = 1
            else:
                count += 1

        if count == 8:
            print("Time is fully booked")
            option = input("Another Time? ")
            if option == "Y":
                time = int(input("Enter here your new time: "))
            else:
                break
        else:
            courtOption = int(input("Which of the court options would you like to book?")) - 1
        
    while enter:
        Schedule(courtOption,time)
        amount[0][time] += 1
        amount[1][courtOption] += 1
        print("Court Succesfully Booked")
        print("The court booked will be: ",courtOption+1)
        for i in range(0,3):
            print(corresponding[i],": ",guests[-1][i])
        enter = False
    
def Action3():
    for j in range(0,10):
        print("Hour: ",hours[j],":00 to",(hours[j]+1),":00")
        print(" ")
        for i in range(0,8):
            print("Court ",i+1,": ", end = " ")
            Availability(i,j)
        print(" ")

Action3()
while day != "Y":
    print("To Schedule a Guest enter \'1\'\nTo check the availability for a specific time enter \'2\'\nTo look the availability for all courts at all times enter \'3\'\nFor none of these option enter \'4\'")
    print(" ")
    choice = int(input("Enter your choice here: "))
    if choice == 1:
        x = 1
        while x:
            x = CourtSchedule()
    elif choice == 2:
        check = int(input("Enter the starting hour of the time you want to check: "))
        store = 0
        store = timeArray(check)
        for i in range(0,8):
            print("Court: ",i+1)
            Availability(i,store)
        
    elif choice == 3:
        Action3()
        
    day = input("Is the day over yet?")

print("")
print("MOST BOOKINGS: ")

for j in range(0,2):
    print(" ")
    for i in range(0,len(amount[j])):
        if amount[j][i] > most[j]:
            most[j] = amount[j][i]

    if most[j]:
        print("The ",names[j]," hour(s) with most bookings were... ")
        if j == 0:
            add = 7
        else:
            add = 0
            
        for i in range(0,len(amount[j])):
            if amount[j][i] == most[j]:
                print(names[j],i+1+add)
        print("... with a total of ",most[j],"booking(s)")
    else:
        print(names[j],": None, There were no bookings")
        
print("")

for i in range(0,8):
    totalNumber += amount[1][i]

print("Total number of bookings was ",totalNumber)
