#1
name = input("Enter your name: ")
if name == 'Hazel':
    print("Hello Hazel")
else:
    print("We Haven't Met")

#2
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

#3 
""" ph| OUTPUT
-1| Error... enter a number from 0 to 14
 0| pH is acidic
 7| pH is neutral
15| Error... enter a number from 0 to 14 """

#4
""" print("Select one of the following options")
print("Enter A for Multiply")
print("Enter B for Divide")
print("Enter C for Add")
print("Enter D for Subtract")
print("Enter E for Remainder Division")

option = input("Enter the corresponding letter here: ")
number1 = int(input("Enter your number here: "))
number2 = int(input("Enter your second number here: "))

Case based on option
    Case "A":
        print(number1*number2)
        break
    Case "B":
        print(number1/number2)
        break
    Case "C":
        print(number1+number2)
        break
    Case "D":
        print(number1-number2)
        break
    Case "E":
        print(number1%number2)
        break
    default:
        print("Invalid Choice")
End Case """

#5
""" Year = input("Enter the year you want to check here: ")
LeapYear = FALSE
IF (mod(Year, 4)=0) THEN
LeapYear = TRUE
END IF
IF (mod(Year,100) = 0 THEN
LeapYear = FALSE
END IF
IF (mod (Year,400)) = 0 THEN
LeapYear = TRUE
END IF
    
if (LeapYear):
    print("Is a LeapYear")
else:
    print("Not a LeapYear")
    
ii) It is necessary in order to declare the variable. If none of the if's
conditions are met, then that will be the value for leapYear. Otherwise
it would have been left undefined and an error message would appear.

Year|Expected Output
1800| Not a LeapYear
1986| Not a LeapYear
2000| Is a LeapYear
2016| Is a LeapYear """
