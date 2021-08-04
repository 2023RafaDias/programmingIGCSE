import random

#stores the guest position + 1 or 0 if it is free
courts = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]

corresponding = ["code","name","phone"]
guests = []

hours = [8,9,10,11,12,13,14,15,16,17,18]

day = "started"
print("Day Has Started")
print(" ")

#finds the time position correspondant to user's entry
def timeArray(selected):
    for i in range(0,10):
        if selected == hours[i]:
            return int(i)

#checks if a specific court is free at a specific time
def Availability(i,j):
    if not(courts[i][j]):
        print("Free")
    else:
        print("booked")
        position = courts[i][j]-1
        for i in range(0,3):
            print(corresponding[i],": ",guests[position][i])
        
        

#checks what courts are free at a specific time
def CheckTime(selected):
    store = 0
    store = timeArray(selected)
    for i in range(0,8):
        print("Court: ",i+1)
        Availability(i,store)

#makes sure that all codes are unique
def CheckUnique():
    rep = len(guests)
    if rep > 1:
        for i in range(0,rep-1):    
            while guests[-1][0] == guests[i][0]:
                guests[-1][0] = random.randint(1000,9999)

#sets up a new guest with info
def Schedule(court,time):
    guests.append([])                          
    guests[-1].append(1890)
    CheckUnique()
    name = input("What is the guest's name?")
    guests[-1].append(name)
    correct = "NO"
    while correct != "Y":
        phone = input("Enter the guest's phone number: ")
        print(phone)
        correct = input("Does the user confirm the number?")
    guests[-1].append(phone)
    courts[court][time] = len(guests)

#schedules the guest and makes sure it is valid
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
        print("Court Succesfully Booked")
        print("The court booked will be: ",courtOption+1)
        for i in range(0,3):
            print(corresponding[i],": ",guests[-1][i])
        enter = False
    
            
            
    #confirm de phone number
    #display the code

def Action1():
    x = 1
    while x:
        x = CourtSchedule()
    
def Action2():
    check = int(input("Enter the starting hour of the time you want to check: "))
    CheckTime(check)

#print availability for courts at all times 
def Action3():
    """for i in range(0,8):
        print("Court ",i+1,"'s availability: ")
        print(" ")
        for j in range(0,10):
            print("Hour: ",hours[j],":00 to",(hours[j]+1),":00")
            Availability(i,j)
        print(" ")"""

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
        Action1()
    elif choice == 2:
        Action2()
    elif choice == 3:
        Action3()
        
    day = input("Is the day over yet?")

#count how many bookings there were
#change so that the attendant is able to seelct the court to be booked.
#display the available courts and then ask user to select one
