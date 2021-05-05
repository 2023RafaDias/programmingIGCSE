movement = ['','','Ground Floor Movement Detected','','','','','First Floor Movement Detected','']

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
        if count == 2 or count == 7:
            print(count+1, ': ',movement[count])

    if count == 9:
        print("Reached the end: Alarm Off")

    again = input("again? y/n ")
