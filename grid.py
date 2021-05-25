grid = []
while True:
    try:
        xsize = int(input("How wide will your grid be: "))
        break
    except ValueError:
        print("Integer Only!")

while True:
    try:
        ysize = int(input("How high will your grid be: "))
        break
    except ValueError:
        print("Integer Only!")

again = "Y"
while True:
    for i in range(0, ysize):
        grid.append([])
        for j in range(0, xsize):
            grid[i].append("X")

    for i in range(0, ysize):
        for j in range(0, xsize):
            print(grid[i][j], end="")
        print("")
    while again == "Y":
        while True:
            try:
                userX = int(input("XCOORD: "))
                break
            except ValueError:
                print("Invalid! Integer Only.")

        if userX > xsize-1 or userX < 0:
            print("Points are out of accepted range... entries should be between 0 and ", xsize-1)
            break

        while True:
            try:
                userY = int(input("YCOORD: "))
                break
            except ValueError:
                print("Invalid! Integer Only.")
        if userY > ysize-1 or userY < 0:
            print("Points are out of accepted range... entries should be between 0 and ", ysize-1)
            break
        userY = xsize - userY

        grid[userY-1][userX] = "O"

        for i in range(0, ysize):
            for j in range(0, xsize):
                print(grid[i][j], end="")
            print("")
        again = input("Again? Use Y: ")
    break
