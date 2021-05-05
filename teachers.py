classHold = []
size = int(input("How many students do you have?"))
count = 1
while len(classHold) != size:
    print("Enter Student ",count,"'s name here: ")
    student = input()
    classHold.append([student])
    classHold[count-1].append([0])
    count+= 1

print(classHold)
print(classHold[0][1][0])

classHold.append([0])
def Test(number,students):
    for i in range (0,len(classHold)):
        print("Enter the test score for test ", number, " here (out of ten) : ")
        score = int(input())
        classHold[i][number][number-1] = score
        classHold[students-1] += score
       

Test(1,size)

print(classHold)
