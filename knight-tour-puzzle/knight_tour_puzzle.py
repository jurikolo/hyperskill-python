# Write your code here
pos = input("Enter the knight's starting position: ")
try:
    x, y = pos.split(sep=" ")
    x = int(x)
    y = int(y)
    assert x in range(1, 9)
    assert y in range(1, 9)
except Exception as e:
    print("Invalid dimensions!")
else:
    print(" -------------------")
    for row in range(8, 0, -1):
        to_print = f"{row}| "
        for column in range(1, 9):
            if (x == column) and (y == row):
                to_print += "X "
            else:
                to_print += "_ "
        to_print += "|"
        print(to_print)
    print(" -------------------")
    print("   1 2 3 4 5 6 7 8 ")
