import random
courts = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]

#[code,"name","phone"]
guests = []

hours = [8,9,10,11,12,13,14,15,16,17,18]

def CheckTime(selected):
    store = 0
    for i in range(0,10):
        if selected == hours[i]:
            store = i
            print(store)
    for i in range(0,8):
        print("Court: ",i+1)
        if not(courts[i][store]):
            print("Free")

def Availability(i,j):
    if not(courts[i][j]):
        print("Free")
    else:
        print("booked")

for i in range(0,8):
    print("Court ",i+1,"'s availability: ")
    print(" ")
    for j in range(0,10):
        print("Hour: ",hours[j],":00 to",(hours[j]+1),":00")
        Availability(i,j)
    print(" ")

def Schedule(court,time):
    guests.append([])
    guests[-1].append(random.randint(1000,9999))
    name = input("What is the guest's name?")
    guests[-1].append(name)
    phone = input("What is the guest's phone number?")
    guests[-1].append(phone)
    courts[court][time] = len(guests)

Schedule(7,3)
print(courts[7])
print(guests)
