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
        size = len(string)
        firstname,surname = string[0], string[size-1]
        print(surname,firstname[0])
        print("Firstname is ",firstname)
        amount = len(firstname)
        for i in range(amount-1,-1,-1):
            firstnameRev += firstname[i]
            for x in range(10):
                if vowels[x] in firstname[i]:
                    vowel+=1
        print("Amount of vowels is ", vowel)
        print("Reversed is ", firstnameRev.upper())
        again = "Y"
        while again == "Y":
            search = input("Search for a specific letter: ")
            if len(search) > 1:
                print("please use only one character")
            else:
                searchRes = 0
                for i in range(amount-1,-1,-1):
                    if search.lower() in firstname[i]:
                        searchRes += 1
                    if search.upper() in firstname[i]:
                        searchRes+= 1
                print("amount: ",searchRes)
            again = input("Another search? Use Y/N ")
    repeat = input("Again? Use Y/N")
