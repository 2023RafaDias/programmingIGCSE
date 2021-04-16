TIME = 0
LIMIT = 0
STRIKE = 0
TEMPERATURE = ["","","","","","","","","","","","","","","","","",""]
BABY = ""
BABY = input("Is there a Baby to monitor the temperature? Use Y for yes: ")
while BABY = "Y":
    while TIME < 18:
        LIMIT = input("Has ten minutes passed? Use Y for yes: ")
        while LIMIT == "Y":
            TEMPERATURE[TIME] = input("Please enter the Baby's temperature right now: ")
            if int(TEMPERATURE[TIME]) < 36.0:
                print("Temperature is too low.")
                STRIKE = STRIKE + 1
            elif int(TEMPERATURE[TIME]) >= 37.5:
                print("Temperature is too high.")
                STRIKE = STRIKE + 1
            else:
                print("Temperature is acceptable.")
            TIME = TIME + 1
            LIMIT = "N"

    MAXTEMP = TEMPERATURE[0]
    for i in range (1,17):
        if TEMPERATURE[i] > TEMPERATURE[i-1]:
            MAXTEMP = TEMPERATURE[i]
        else:
            MINTEMP = TEMPERATURE[i]
    print("")
    print("The Maximum Temperature was of ",MAXTEMP,"°C")
    print("")
    print("The Minimum Temperature was of ",MINTEMP,"°C")
    print("")
    RANGE = MAXTEMP-MINTEMP
    print("The range of these values is of ",RANGE)
    
    if RANGE > 1:
        print("The Baby has had a difference of more than one degree in their temperature over the course of 3 hours.")
    if STRIKE > 2:
        print("Temperature of the Baby has been outside the temperature range for more than 2 times over 3 hours")

    BABY = input("Do you want to start monitoring again? Use Y for yes: ")
