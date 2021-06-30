courts = [[0,0,0,0,0,0,0,0,0,0,"free"],[0,0,0,0,0,0,0,0,0,0,"free"],[0,0,0,0,0,0,0,0,0,0,"free"],[0,0,0,0,0,0,0,0,0,0,"free"],[0,0,0,0,0,0,0,0,0,0,"free"],[0,0,0,0,0,0,0,0,0,0,"free"],[0,0,0,0,0,0,0,0,0,0,"free"],[0,0,0,0,0,0,0,0,0,0,"free"]]

guests = [[0,0,"name","phone"]]

hours = [8,9,10,11,12,13,14,15,16,17,18]

def Free(number):
    free = 0
    for i in range (0,8):
        if not(courts[number][i]):
            free += 1
    courts[number][8] = free
    return free

for i in range(0,8):
    print("Court ",i+1,"'s availability: ")
    print(" ")
    for j in range(0,10):
        print("Hour: ",hours[j],":00 to",(hours[j]+1),":00")
        if not(courts[i][j]):
            print("Free")
    print(" ")

def CheckTime(selected):
    store = 0
    for i in range(0,10):
        if selected == hours[i]:
            store = i
            print(store)
    for i in range(0,8):
        print("Court: ",i+1,"\n Hour: ",selected)
        if not(courts[i][store]):
            print("Free")

selected = input("What time would you like?")
CheckTime(selected)
