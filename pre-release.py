import random

#stores the guest position + 1 or 0 if it is free
courts = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]

corresponding = ["code","name","phone"]
guests = []

hours = [8,9,10,11,12,13,14,15,16,17,18]

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

def CheckUnique():
    rep = len(guests)
    print(rep)

    if rep > 1:
        for i in range(0,rep-1):    
            while guests[-1][0] == guests[i][0]:
                guests[-1][0] = random.randint(1000,9999)
    
def Schedule(court,time):
    guests.append([])                          
    guests[-1].append(1890)
    CheckUnique()
    name = input("What is the guest's name?")
    guests[-1].append(name)
    phone = input("What is the guest's phone number?")
    guests[-1].append(phone)
    courts[court][time] = len(guests)

def CourtSchedule():
    courtOption = int(input("What court are you booking?"))
    timeOption = int(input("At what time would you like to book?"))
    time = timeArray(timeOption)
    
    if not(courts[courtOption-1][time]):
        Schedule(courtOption-1,time)
        return 0
    else:
        print("Court already booked at given time \n Try Again.")
        return 1

#print availability for courts at all times 
for i in range(0,8):
    print("Court ",i+1,"'s availability: ")
    print(" ")
    for j in range(0,10):
        print("Hour: ",hours[j],":00 to",(hours[j]+1),":00")
        Availability(i,j)
    print(" ")

x = 1
while x:
    x = CourtSchedule()

CheckTime(8)

x = 1
while x:
    x = CourtSchedule()

CheckTime(10)

