material = ["C","G","S"]
weight = [[24.9,25.1],[49.9,50.1],[49.9,50.1]]
n = -2
choices = ["","","",""]
new = "Y"
rejected = 0
order = [0,0,0]
total_weight = 0
discount = 0
amount = 0
while new == "Y":
    choices.append(0)
    choices.append(0)
    n += 2
   
    while choices[n] not in material:
        choices[n] =(input("Enter your material: "))

    print("Material ok")

    for i in range (0,3):
        if choices[n] ==  material[i]:
            count = i
       
    a = 1
    while a==1:
        try:
            choices[n+1] = float(input("Please enter the parcel's weight: "))
            a = 0
        except ValueError:
            print("integer only!")

    if choices[n+1] < weight[count][0] or choices[n+1] > weight[count][1]:
        print("Parcel rejected: invalid weight")
        print("Sack information: ",choices[n],", ",choices[n+1])
        choices[n],choices[n+1]=0,0
        rejected += 1
        n = -2
    else:
        print("Parcel ok")
        print("Sack information: ",choices[n],", ",choices[n+1])
        while a==0:
            try:
                amount = int(input("How many sacks of this type would you like?"))
                a = 1
            except ValueError:
                print("integer only!")
    for i in range (0,amount
                    ):
        order[count]+= 1
        total_weight += choices[n+1]

    new = input("Is there another TYPE OF sack?")

print("the order's total weight was of ", total_weight)
print("the number of sacks rejected was ", rejected)

prices = [3,2,2]
cost = 0
for i in range (0,3):
    cost += order[i]*prices[i]

print("the total cost was of ", cost)

discount = order[1]/2
if discount>order[2]/2:
    discount = order[2]/2
if discount>order[0]:
    discount = order[0]

print("Your discount was of ",discount)
print("the cost with discount = ",cost-discount)
