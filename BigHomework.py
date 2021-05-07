name = input("Enter your name: ")
if name == 'Hazel':
    print("Hello Hazel")
else:
    print("We Haven't Met")



temp = int(input("Enter the temperature: "))
humidity = int(input("Enter the humidity"))
windows = ""
while windows != 'y' and windows != 'n':
    windows = input("Is window closed? y/n")
if temp > 25 or humidity > 50 and windows == 'y':
    print("Open Window")
elif temp < 10 or humidity < 50 and windows == 'n':
    print("Close Window")
else:
    print("Window Okay")

#OUTPUT Select one of the following options”
#OUTPUT “Enter A for Multiply”
#OUTPUT “Enter B for Divide”
#OUTPUT “Enter C for Add”
#OUTPUT “Enter D for Subtract”
#OUTPUT “Enter E for Remainder Division”
