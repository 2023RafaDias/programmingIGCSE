vowels = "aeiou"
vowelNum = 0
consonantNum = 0
vowelInclude = ""
consonantInclude = ""
sentence = input("Please enter your word/sentence here: ")
for i in range(0,len(sentence)):
    print(i)
    for x in range(0,len(vowels)):
        print(x)
        include = ""
        if vowels[x] in sentence[i]:
            vowelInclude += sentence[i]
            vowelNum += 1
            print("yes",sentence[i],vowels[x])
            include = "no"
        elif vowels[x].upper() in sentence[i]:
            vowelInclude += sentence[i]
            vowelNum += 1
            print("yes upper",sentence[i],vowels[x])
            include= "no"
        if include == "":
            consonantInclude += sentence[i]
            consonantNum += 1
            print("no",sentence[i],vowels[x])


print(vowelNum)
print(consonantNum)
print(vowelInclude)
print(consonantInclude)

