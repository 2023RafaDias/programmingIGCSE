positions = []
number = str(input("Enter a number: "))

size = len(number)
while len(positions) < size:
    positions.append(0)

def Positions(n):
    for i in range (size-1,-1,-1):
        positions[i] = (n//10**i)*10**i
        n = n%10**i
        if i == 0:
            break

try:
    numberInt = int(number)
    error = "no"
    Positions(numberInt)

except ValueError:
    print("Invalid, an integer must be entered")
    error = "yes"

for i in range(size-1,-1,-1):
    print(positions[i])
