while True:
    name = input("What is your name? ")
    base = int(input("What is the base? "))
    start = int(input("Where would you like to start: "))
    end = int(input("Where would you like to end: "))
    print("Hi, ",name,", here is your time table")

    def multiples(base,start):
        print(base,"x",start,"=",base*start)

    while start != end+1:
        multiples(base,start)
        start += 1

    again = input("again? Use Y: ")
    if again != "Y":
        break
