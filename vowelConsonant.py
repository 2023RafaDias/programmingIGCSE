vowels = "aeiou"
vowelNum = 0
consonantNum = 0
vowelInclude = ""
consonantInclude = ""
sentence = input("Please enter your word/sentence here: ")
sentence = sentence.replace(" ","")
for i in range(0,len(sentence)):
    for x in range(0,len(vowels)):
        include = ""
        if vowels[x] in sentence[i]:
            vowelInclude += sentence[i]
            vowelNum += 1
            include = "no"
            break
        elif vowels[x].upper() in sentence[i]:
            vowelInclude += sentence[i]
            vowelNum += 1
            include = "no"
            break
        elif include != "no" and x == 4:
            consonantInclude += sentence[i]
            consonantNum += 1


print("The number of vowels is:",vowelNum)
print("The number of consonants is:",consonantNum)
print("Only the vowels are:",vowelInclude)
print("Only the consonants are:",consonantInclude)

