def BinaryToDecimal():
    ENT = "YES"
    while ENT != "no":
        TOTAL = 0
        NUMBER = input("please enter your number: ")
        X = len(NUMBER)
        COUNT = 0
        for I in range (X-1,-1,-1):
            if int(NUMBER[I]) > 1:
                COUNT = COUNT + 1
        while COUNT == 0:
            EXP = 0
            for i in range(X-1, -1,-1):
                N = 2**EXP
                TOTAL = TOTAL + int(NUMBER[i])*N
                EXP = EXP + 1
                print("Your number in denary is ",TOTAL)
                COUNT = -1
        while COUNT >= 1:
                print("Invalid. Please Enter Binary numbers only: ")
                COUNT = -1
                ENT = input("Would you like to try again binary to denary? To stop use: no ")
def DecimalToBinary():
    ENT = "YES"
    while ENT != "no":
        TOTAL = 0
        NUMBER = int(input("please enter your number: "))
        COUN1 = 0
        N2 = 0
        N = NUMBER
        if NUMBER == 1:
            TOTAL = 1
        while N != 1:
            COUN1 = COUN1 + 1
            N = N//2
        for i in range(0,COUN1+1):
            N2 = NUMBER%2
            EXP = 10**i
            TOTAL = TOTAL + N2*EXP
            NUMBER = NUMBER//2
        print("Your number in BINARY is ",TOTAL)
        ENT = input("Would you like to try again denary to binary? To stop use: no ")      
               
ENTER = " "
while ENTER != "no":
    OPTION = input("Are you converting a number in denary or binary? ")
    if OPTION == "binary":
        BinaryToDecimal()
    elif OPTION == "denary":
        DecimalToBinary()
    else:
        input("Invalid, please use binary or dinary: ")
    ENTER = input("Would you like to convert in another order? To stop use: no ")
