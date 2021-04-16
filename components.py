COMPONENTS = ["ALU","BUS","CONTROL UNIT","MAR","MDR","RAM","REGISTERS"]
DEFINITIONS = ["Arithmetic & Logic Unit", "There are three buses", "Part of the Von Neumann deisgn", "Memory Address Register", "Memory Data Register", "Random Access Memory", "Will hold a tiny amount of data"]
ANSWER = 'Y'
print("KNOWLEDGE IMPARTER")
while ANSWER != "N":
    VALUE = 0
    print("Please enter an acceptable component...")
    COMP = input("Which component do you request?")

    for i in range (0,7):
        if COMP in COMPONENTS[i]:
            print(DEFINITIONS[i])
            OK = " "
        else:
            VALUE = VALUE + 1

    if VALUE == 7:
        print("Invalid Component")

    while OK != "N":
        ANSWER = input("Would you like to use another component? To stop use N: ")
        OK = "N"
