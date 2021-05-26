import math

def Calculator():
    while True:
        try:
            n1 = int(input("Enter first number here: "))
            n2 = int(input("Enter second number here: "))
            break
        except ValueError:
            print("Inavlid Entry! Please enter an integer")

    
    print("1 - Addition \n 2- Subtraction \n 3- Multiplying \n 4- Dividing")
    option = input("Enter your choice here")

    if option == "1":
        x = n1+n2
    elif option == "2":
        x = n1-n2
    elif option == "3":
        x = n1*n2
    elif option == "4":
        x = n1/n2
    else:
        print("No valid option entered")

    print(x)

    rounding = input("Would you like to round your result? Use Y for yes: ")

    if rounding == "Y":
        x = round(x)
        print(x)

    if x >= 0:
        squareroot = input("Would you like to sqaureroot your result? Use Y for yes: ")
        if squareroot == "Y":
            x = math.sqrt(x)
            print(x)

    if x <= 143859 and x >= 0:
        x = int(x)
        print("The corresponding ASCII/UNICODE character for the value is ","\" ",chr(x),"\"")
        return x

    
def Check(char):
    for i in range(0,len(name)):
        if char == name[i]:
            print(ord(char))
            
def NameCalc():
    name = input("Enter here your name: ")
    print("The length of your name is: ",len(name))
    while True:
        check = input("Would you like to check the ASCII value for one of the characters? ")
        Check()
        again = input("Again? Use Y for yes: ")
        if again != "N":
            break

while True:
    calc = input("Would you like to enter the Calculator or the Name Calculator? Use C or N: ")

    if calc == "C":
        Calculator()
    elif calc == "N":
        NameCalc()
    else:
        print("Invalid Option!")

    again = input("Again? Use Y for Yes: ")
    if again != "Y":
        break

    
    
    

    
    
    
