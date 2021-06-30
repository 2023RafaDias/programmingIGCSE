time = ["midday","midnight"]
dataLogger = []
def NewTemp(i):
    print("Temp for ",time[i])
    while True:
        try:
            temp = float(input("Enter here: "))
            if temp > 60:
                print("Invalid Temperature. Too Hot")
            elif temp < -60:
                print("Invalid Temperature. Too Cold")
            else:
                break

        except ValueError:
            print("Invalid Temperature. Enter float number only.\nTry Again.")
    
    dataLogger[-1].append(temp)

for i in range(0,30):
    print("Day",i+1)
    dataLogger.append([])
    for i in range(0,2):
        NewTemp(i)
