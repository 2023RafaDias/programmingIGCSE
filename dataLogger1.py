time = ["midday","midnight"]
dataLogger = []
answer = "Y"

while answer == "Y":
    dataLogger.append([[]])
    dataLogger[-1].append([])
    total = [0,0]
    dayMax = -60
    nightMin = 60

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
            if dataLogger[-1][0][-1]>dayMax:
                dayMax = dataLogger[-1][0][-1]
            if dataLogger[-1][1][-1]<nightMin:
                nightMin = dataLogger[-1][1][-1]

    print("The Average Midday Temperature was of ",round(total[0]/30,2),"°C")
    print("The Average Midnight Temperature was of ",round(total[1]/30,2),"°C")
    print("The maximum midday temperature was ",dayMax)
    print("The minimum midnight temperature was ",nightMin)

    answer = input("Next Month? Y/N: ")
