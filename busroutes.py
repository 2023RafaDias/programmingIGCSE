BUSA = ["","","","","","","","","","","","","","","","","","","",""]
BUSB = ["","","","","","","","","","","","","","","","","","","",""]
BUSC = ["","","","","","","","","","","","","","","","","","","",""]
BUSD = ["","","","","","","","","","","","","","","","","","","",""]
BUSE = ["","","","","","","","","","","","","","","","","","","",""]
BUSF = ["","","","","","","","","","","","","","","","","","","",""]
DAYS = ["Mon1","Tue1","Wed1","Thu1","Fri1","Mon2","Tue2","Wed2","Thu2","Fri2","Mon3","Tue3","Wed3","Thu3","Fri3","Mon4","Tue4","Wed4","Thu4","Fri4"]
ROUTES = ["BUSA","BUSB","BUSC","BUSD","BUSE","BUSF"]
NUMBERDAYS_A = 0
NUMBERDAYS_B = 0
NUMBERDAYS_C = 0
NUMBERDAYS_D = 0
NUMBERDAYS_E = 0
NUMBERDAYS_F = 0
X = 0
Y = 0

TOTALA = 0
TOTALB = 0
TOTALC = 0
TOTALD = 0
TOTALE = 0
TOTALF = 0

for i in range (0,20):
    print("Please enter the data for BUS A on the day ",DAYS[i]," below")
    BUSA[i]=input("Please Enter Here: ")
    if int(BUSA[i]) < 0:
        NUMBERDAYS_A = NUMBERDAYS_A + 1
        TOTALA = TOTALA + int(BUSA[i])
    
for i in range (0,20):
    print("Please enter the data for BUS B on the day ",DAYS[i]," below")
    BUSB[i]=input("Please Enter Here: ")
    if int(BUSB[i]) < 0:
        NUMBERDAYS_B = NUMBERDAYS_B + 1
        TOTALB = TOTALB + int(BUSB[i])
        
for i in range (0,20):
    print("Please enter the data for BUS C on the day ",DAYS[i]," below")
    BUSC[i]=int(input("Please Enter Here: "))
    if BUSC[i] < 0:
        NUMBERDAYS_C= NUMBERDAYS_C + 1
        TOTALC = TOTALC + int(BUSC[i])
        
for i in range (0,20):
    print("Please enter the data for BUS D on the day ",DAYS[i]," below")
    BUSD[i]=int(input("Please Enter Here: "))
    if BUSD[i] < 0:
        NUMBERDAYS_D = NUMBERDAYS_D + 1
        TOTALD = TOTALD + int(BUSD[i])
        
for i in range (0,20):
    print("Please enter the data for BUS E on the day ",DAYS[i]," below")
    BUSE[i]=int(input("Please Enter Here: "))
    if BUSE[i] < 0:
        NUMBERDAYS_E = NUMBERDAYS_E + 1
        TOTALE = TOTALE + int(BUSE[i])
        
for i in range (0,20):
    print("Please enter the data for BUS F on the day ",DAYS[i]," below")
    BUSF[i]=int(input("Please Enter Here: "))
    if BUSF[i] < 0:
        NUMBERDAYS_F = NUMBERDAYS_F + 1
        TOTALF = TOTALF + int(BUSF[i])
        
NUMBERDAYS=[NUMBERDAYS_A,NUMBERDAYS_B,NUMBERDAYS_C,NUMBERDAYS_D,NUMBERDAYS_E,NUMBERDAYS_F]
TOTAL=[TOTALA,TOTALB,TOTALC,TOTALD,TOTALE,TOTALF]
for i in range(0,6):
    print("This is information on ",ROUTES[i])
    print("This bus was ",NUMBERDAYS[i]," late.")
    print("Resulting in a total of ",TOTAL[i], " minutes late.")
    print("")

USEROPTION = input("If you want to know the data for a specific day please press Y: ")
while USEROPTION == "Y":
    DAYCHOICE = input("Please Enter the date you want to look at: ")
    for i in range (0,20):
        if DAYCHOICE == DAYS[i]:
            if int(BUSA[i]) > 0:
                print("Bus A was ",BUSA[i]," minutes late in ",DAYS[i])
                Y = Y + 1
            if int(BUSB[i]) > 0:
                print("Bus B was ",BUSB[i]," minutes late in ",DAYS[i])
                Y = Y + 1
            if int(BUSC[i]) > 0:
                print("Bus C was ",BUSC[i]," minutes late in ",DAYS[i])
                Y = Y + 1
            if int(BUSD[i]) > 0:
                print("Bus D was ",BUSD[i]," minutes late in ",DAYS[i])
                Y = Y + 1
            if int(BUSE[i]) > 0:
                print("Bus E was ",BUSE[i]," minutes late in ",DAYS[i])
                Y = Y + 1
            if int(BUSF[i]) > 0:
                print("Bus F was ",BUSF[i]," minutes late in ",DAYS[i])
                Y = Y + 1
            print("There were a total of", Y, " buses late.")
        else:
            print("Invalid Option")
    USEROPTION = input("If you would like to try again please enter Y: ")
