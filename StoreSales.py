outletName = []
sales = []
quarter = [0,0,0,0]
month = ["january-march","april-june","july-september","october-december"]

stores = int(input("How Many stores are there: "))
for i in range(0,stores):
    print("What is the name of the ",i+1," outlet?")
    outletName.append(input("Enter Here: "))
    sales.append([0])
    for j in range(0,4):
        print("What was the sales quantity to the nearest thousand on ",month[j],"?")
        sales[i].append(int(input("Enter Here: ")))
        sales[i][0] += sales[i][-1]
        quarter[j] += sales[i][-1]

minimum = sales[0][1]
maximum = sales[0][1]
indexes = [[0,0],[0,0]]

print(" ")
for i in range(0,stores):
    print("Total for",outletName[i],": ",sales[i][0])
    for j in range(1,5):
        if sales[i][j]< minimum:
            minimum = sales[i][j]
            indexes[0][0] = i
            indexes[0][1] = j-1
        elif sales[i][j]> maximum:
            maximum = sales[i][j]
            indexes[1][0] = i
            indexes[1][1] = j-1

print(" ")
for i in range(0,4):
    print("Total for quarter",i+1,":",quarter[i])

print(" ") 
print("The smallest sale was in: ",outletName[indexes[0][0]],"\n With a total of",minimum,"in",month[indexes[0][1]])
print("The largest sale was in: ",outletName[indexes[1][0]],"\n With a total of",maximum,"in",month[indexes[1][1]])
