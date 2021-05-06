classHold = []
average = []
size = int(input("How many students do you have? "))
count = 1
while len(classHold) != size:
    print("Enter Student ",count,"'s name here: ")
    student = input()
    classHold.append([student])
    classHold[count-1].append([])
    count+= 1

def Test(number):
    average.append([])
    average[number-1].append(0)
    average[number-1].append(0)
    for i in range (0,len(classHold)):
        print("Enter the test score for test ", number, " here (out of ten) : ")
        score = int(input())
        average[number-1][0] += score
        classHold[i][1].append(score)
    average[number-1][1] =(average[number-1][0]/len(classHold))

loop = int(input("How many tests were there?"))
allTests = 0

for i in range(0,loop):
    Test(i+1)
    allTests += average[i][0]
    print("Average of Test", i+1, "was of ",average[i][1])

print("Average of all Tests was of ",allTests/(size*loop))
        
for i in range(0,size):
    amount = 0
    classHold[i][1].append(0)
    for ii in range(0,loop):
        add = classHold[i][1][ii]
        amount += int(add)
        classHold[i][1][size] = amount/loop
    print("Student ",classHold[i][0],"'s avg grade of the year was of ",classHold[i][1][size])
    if classHold[i][1][size] <= 6:
        classHold[i][1].append("not pass")
        print("Student ",classHold[i][0],"did ",classHold[i][1][len(classHold)+1])
        for ii in range(0,loop):
            if classHold[i][1][ii] < 5:
                print("Test ",ii+1,"needs to be retaken by ",classHold[i][0])
    else:
        classHold[i][1].append("pass")
        print("Student ",classHold[i][0],"did ",classHold[i][1][len(classHold)+1])
        for ii in range(0,loop):
            if classHold[i][1][ii] < 5:
                print("However, Test ",ii+1,"needs to be retaken by ",classHold[i][0])

from tabulate import tabulate
print(tabulate(classHold[0], classHold[1], headers=['Name', 'Age']))
