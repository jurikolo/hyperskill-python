# Calculate how many characters required for each space
def calculate_delimiter_multiplier(x, y):
    spaces = x * y
    result = 1
    while spaces > 9:
        spaces /= 10
        result += 1
    return result

# Calculate
def calculate_delimiter(some_num):
    result = 1
    while some_num > 9:
        some_num /= 10
        result += 1
    return result

def get_dashes(delimiter_multiplier, y_delimiter, board_y):
    result = " " * y_delimiter
    result += "--"  # first dash
    result += "-" * (board_y * (delimiter_multiplier + 1))
    result += "-"  # last dash
    return result

def get_row_prefix(y, y_delimiter):
    return " " * (y_delimiter - len(str(y))) + str(y)

def get_footer(delimiter_multiplier, y_delimiter, board_y):
    result = " " * y_delimiter + " "
    for x in range(1, board_y + 1):
        result += " " + " " * (delimiter_multiplier - calculate_delimiter(x)) + str(x)
    return result

# Initialize board
while True:
    board = input("Enter your board dimensions: ")
    try:
        board_y, board_x = board.split(sep=" ")
        board_x = int(board_x)
        board_y = int(board_y)
        assert board_x >= 0
        assert board_y >= 0
    except Exception:
        print("Invalid dimensions!")
    else:
        break

# Initialize starting position
while True:
    pos = input("Enter the knight's starting position: ")
    try:
        pos_x, pos_y = pos.split(sep=" ")
        pos_x = int(pos_x)
        pos_y = int(pos_y)
        assert pos_x in range(1, board_x + 1)
        assert pos_y in range(1, board_y + 1)
    except Exception:
        print("Invalid dimensions!")
    else:
        break

del_mult = calculate_delimiter_multiplier(board_x, board_y)
y_delimiter = calculate_delimiter(board_y)

# Print the board
print(get_dashes(del_mult, y_delimiter, board_y))
for row in range(board_x, 0, -1):
    to_print = f"{get_row_prefix(row, y_delimiter)}| "
    for column in range(1, board_y + 1):
        if (pos_x == column) and (pos_y == row):
            to_print += " " * (del_mult - 1) + "X "
        else:
            to_print += ("_" * del_mult) + " "
    to_print += "|"
    print(to_print)
print(get_dashes(del_mult, y_delimiter, board_y))
print(get_footer(del_mult, y_delimiter, board_y))
