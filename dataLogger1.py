time = ["midday","midnight"]
dataLogger = []
dataLogger.append([[]])
dataLogger[-1].append([])
total = [0,0]
dayMax = 0
nightLow = 0

print(dataLogger)

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

    dataLogger[-1][i].append(temp)
    

for i in range(0,30):
    print("Day",i+1)
    for j in range(0,2):
        NewTemp(j)
        total[j] += dataLogger[-1][j][-1]
    if i >1:
        if dataLogger[-1][0][-1]>dataLogger[-1][0][-2]:
            dayMax = dataLogger[-1][0][-1]
        if dataLogger[-1][1][-1]<dataLogger[-1][1][-2]:
            nightLow = dataLogger[-1][1][-1]

print("The Average Midday Temperature was of ",total[0]/30,"°C")
print("The Average Midnight Temperature was of ",total[1]/30,"°C")
print(dayMax)
print(nightLow)



print(dataLogger)
