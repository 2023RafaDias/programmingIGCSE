votes = []
candidatesNumber = []
answer = "no"
while answer == "no":
    try:
        question = int(input("How Many Canditates Are There? "))
        error = "no"
    except:
        print("invalid entry. must be integer ")
        error = "yes"
       
    if error != "yes":
        if question > 4 or question < 2:
            print("invalid entry. 2 =< x <= 4")
            answer = "no"
        else:
            answer = "yes"

confirm = ""
while confirm != "yes":
    candidates = []
    for i in range (1,question+1):
        candidates.append(input("Enter the name of the candidate. One at a time: "))
        candidatesNumber.append(i)
        votes.append(0)
        x = i
    for i in range (0,question):
        print(candidates[i],candidatesNumber[i])
    confirm = input("Do you confirm these canditates? Use yes or no: ")

while answer == "yes":
    try:
        question = int(input("How Many Voters Are There?"))
        error = "no"
    except:
        print("invalid entry. must be integer ")
        error="yes"

    if error != "yes":
        if question > 30 or question < 1:
            print("invalid entry. 1 =< x <= 30")
            answer = "yes"
        else:
            answer = "no"

entries = 0
while entries != question:
        invalid = 0
        vote = ""
        while vote == "":
            print("Voter ",entries+1," please enter the number of your respective candidate")
            vote = input("Enter Here: ")
           
        for i in range(0,x):
            if str(vote) in str(candidatesNumber[i]):
                votes[i]+=1
                entries += 1
                z = i
            else:
                invalid += 1
            y = i+1
        if invalid == y:
            print("your vote was invalid: please enter a valid candidate number")
        else:
            print("Candidate voted was: ",candidates[z])

officialMax = -1
for i in range(0,x-1):
    if votes[i]<votes[i+1]:
        votes[i],votes[i+1] = votes[i+1],votes[i]
        candidates[i],candidates[i+1] = candidates[i+1],candidates[i]
        maximum = candidates[i+1]
        maximum = 0
    if votes[i]==votes[i+1]:
        officialMax = 1

for i in range (0,x):
        print(candidates[i],votes[i])

if officialMax == 1:
    print("NO OVERALL WINNER")
elif officialMax == 0:
    print(maximum, " NEW CLASS CAPTAIN")
else:
    print(candidates[0], " NEW CLASS CAPTAIN"
