import time

PERIOD_OF_TIME = int(input("How long the light will be flickering (seconds): "))
timeOn = int(input("For how long will it be on: "))
timeOff = int(input("For how long will it be off: "))
print("Remember: Ctrl C to interrupt program!")

count = 0
start = time.time()
while True :
    try:
        if count%2 == 0:
            print("ON!")
            time.sleep(timeOn)
        else:
            print("OFF!")
            time.sleep(timeOff)
        count += 1
    except KeyboardInterrupt:
        print("Keyboard Interrupt: pressed Ctrl-C")
        break
    
    if time.time() > start + PERIOD_OF_TIME : break
