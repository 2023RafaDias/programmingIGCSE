vowels = "aeiouAEIOU"
repeat = "Y"
search = ""
while repeat == "Y":
    firstnameRev = ""
    vowel = 0
    name = input("Enter your name and surname separated by a space: ")
    if " " not in name:
        error = "yes"
        print("please use a space")
    else:
        string = name.split(" ")
        firstname,surname = string[0], string[1]
        print(firstname[0],surname)
        print("Firstname is ",firstname)
        amount = len(firstname)
        for i in range(amount-1,-1,-1):
            firstnameRev += firstname[i]
            for x in range(10):
                if vowels[x] in firstname[i]:
                    vowel+=1
        print("Amount of vowels is ", vowel)
        print("Reversed is ", firstnameRev)
        search = input("Search for a specific vowel: ")
        again = "yes"
        while again == "yes":
            for i in range(amount-1,-1,-1):
                if search in firstname[i]:
                    searchRes += 1
        print("amount: ",searchRes)
        again = input("Another search? ")
    repeat = input("Again? Use Y/N")
