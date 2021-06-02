import time
import random

while True:
    name = input("What is your name? ")
    base = int(input("What is the base? "))
    start = int(input("Where would you like to start: "))
    end = int(input("Where would you like to end: "))
    print("Hi, ",name,", here is your time table")

    def multiples(base,start):
        print(base,"x",start,"=",base*start)

    while start != end+1:
        multiples(base,start)
        start += 1

    again = input("again? Use Y: ")
    if again != "Y":
        break

def GameMode(base1,base2,score):
    print(base1,"x",base2,"=",end = " ")
    answer = int(input("enter here:"))
    if answer == base1*base2:
        score += 1
        print("WELL DONE! Your answer is CORRECT!")
    else:
        print("Oh No! Your answer is wrong...")
        print("Correct answer = ",base1*base2)
    return score

def Base(level):
    if level == "E":
        base = random.randint(0,10)
    elif level == "M":
        base = random.randint(2,20)
    elif level == "H":
        base = random.randint(2,100)
    return base
    
game = input("Would you like to enter game mode?")
while game == "Y":
    score = 0
    level = input("What difficulty? Easy/Medium/Hard E/M/H: ")
    quest = int(input("Enter the number of questions: "))

        
    print("Game starting in....")
    for i in range(3,0,-1):
        print(i,"...")
        time.sleep(1)
    print("GO!")
    for i in range(0,quest):
        base1 = Base(level)
        base2 = Base(level)
        score = GameMode(base1,base2,score)
    print("THE END")
    print("Your final score was ",score,"/",quest,"\nor ",score/quest*100,"%")
    game = input("Again? Use Y: ")
