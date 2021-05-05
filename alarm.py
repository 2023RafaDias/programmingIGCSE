import random
movement = ['','','','','','','','','']
floor = ["ground floor","first floor"]
values = [0,0]

def select(x,y):
    y = random.randint(0,8)
    x = random.randint(0,8)
    while x == y:
        x = random.randint(0,8)
    if x > y:
        movement[x] = floor[1]+" movement detected"
        movement[y] = floor[0]+" movement detected"
    else:
        movement[x] = floor[0]+" movement detected"
        movement[y] = floor[1]+" movement detected"
    values[0] = x
    values[1] = y
    

def stateAlarm(alarm):
    if alarm == 'n':
        print("Alarm Off")
        error = "break"
    elif alarm != 'n' and alarm != 'y':
        print("Invalid State")
        error = "yes"
    else:
        error = "no"
    return error

again = "y"
while again == "y":
    movement = ['','','','','','','','','']
    select(0,0)
    count = -1
    alarm = "y"
    while alarm == "y" and count < 9:
        print("Alarm On")
        error = 'yes'
        while error == "yes":
            alarm = input("Is alarm on? y/n ")
            error = stateAlarm(alarm)
        if alarm == "break":
            break
        count+= 1
        if count == values[0] or count == values[1]:
            print(count+1, ': ',movement[count])

    if count == 9:
        print("Reached the end: Alarm Off")

    again = input("again? y/n ")
