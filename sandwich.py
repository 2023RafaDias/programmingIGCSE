SIZES = ["small","medium", "large"]
TYPES = ["plain", "seeded", "-"]
LETTUCES = ["no", "yes", "-"]
FILLINGS = ["no", "tomatopickles", "tunacheese"]
QUESTION = ["Enter your size: small, medium or large: ","Enter your bread: plain or seeded: ","Do you want lettuce: yes or no: ","Do you want a filling: no, tomato, pickles, cheese or tuna: ","Do you want another filling: chose from same options above: "]
POSITION = ["Invalid FIRST FILLING option. Please chose again from the options: no, tomato, pickles, tuna and cheese: ","Invalid SECOND FILLING option. Please chose again from the options: no, tomato, pickles, tuna and cheese: "]

def CHECK():
    while ORDER[0] != "small" and ORDER[0] != "medium" and ORDER[0] != "large":
        ORDER[0] = input("Invalid SIZE entry. Please enter small, medium or large : ")

    while ORDER[1] != "seeded" and ORDER[1] != "plain":
        ORDER[1] = input("Invalid BREAD entry. Please enter seeded or plain : ")

    while ORDER[2] != "yes" and ORDER[2] != "no":
        ORDER[2] = input("Invalid LETTUCE choice. Please enter yes or no for lettuce : ")
    
    for i in range (0,2):
        while ORDER[3+i] != "no" and ORDER[3+i] != "tomato" and ORDER[3+i] != "pickles" and ORDER[3+i] != "tuna" and ORDER[3+i] != "cheese":
            ORDER [3+i] = input(POSITION[i])

ANSWER = " "
while ANSWER != "no":
    ORDER = ["","","","",""]
    BASE = 3
    COUNT = 0
    for i in range (0,5):
        ORDER[i] = input(QUESTION[i])

    CHECK()
    
    for i in range (0,3):
        if ORDER[0] == SIZES[i]:
            BASE = BASE + i
        if ORDER[1] == TYPES[i]:
            BASE = BASE + i
        if ORDER[2] == LETTUCES[i]:
            BASE = BASE + i
        if ORDER[3] in FILLINGS[i]:
            BASE = BASE + i
        if ORDER[4] in FILLINGS[i]:
            BASE = BASE + i

        print("Total order is $",BASE)
        ANSWER = input("Would you like to make a new order? To stop use: no")
