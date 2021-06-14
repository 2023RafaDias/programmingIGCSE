time = ["midday","midnight"]
dataLogger = []
def NewTemp(i):
    print("Temp for ",time[i])
    temp = float(input("Enter here: "))
    dataLogger[-1].append(temp)

for i in range(0,30):
    print("Day",i+1)
    dataLogger.append([])
    for i in range(0,2):
        NewTemp(i)
