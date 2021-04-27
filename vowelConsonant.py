vowels = "aeiou"
vowelNum = 0
consonantNum = 0
vowelInclude = ""
consonantInclude = ""
sentence = input("Please enter your word/sentence here: ")
for i in sentence:
    for x in range(0,len(vowels)):
        if vowels[x] in sentence[x]:
            vowelInclude += sentence[x]
            vowelNum += 1
        elif vowels[x].upper() in sentence[x]:
            vowelInclude += sentence[x]
            vowelNum += 1
        else:
            consonantInclude += sentence[x]
            consonantNum += 1

print(vowelNum)
print(consonantNum)
print(vowelInclude)
print(consonantInclude)

