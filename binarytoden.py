ENTER = "YES"
while ENTER != "no":
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
                              print("Invalid. Please Enter Binary numbers only.")
                              COUNT = -1

               ENTER = input("Would you like to try again? ")
