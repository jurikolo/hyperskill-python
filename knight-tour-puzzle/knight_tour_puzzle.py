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


def get_dashes(delimiter_multiplier, y_delimiter, board_x):
    result = " " * y_delimiter
    result += "--"  # first dash
    result += "-" * (board_x * (delimiter_multiplier + 1))
    result += "-"  # last dash
    return result


def get_row_prefix(y, y_delimiter):
    return " " * (y_delimiter - len(str(y))) + str(y)


def get_footer(delimiter_multiplier, y_delimiter, board_y):
    result = " " * y_delimiter + " "
    for x in range(1, board_y + 1):
        result += " " + " " * (delimiter_multiplier - calculate_delimiter(x)) + str(x)
    return result


def get_possible_moves(x, y, board_y, board_x, occupied_spaces):
    dirty_moves_list = [[x + 1, y + 2], [x + 1, y - 2], [x + 2, y + 1], [x + 2, y - 1],
                        [x - 1, y + 2], [x - 1, y - 2], [x - 2, y + 1], [x - 2, y - 1]]
    moves_list = []
    for move in dirty_moves_list:
        if (0 < move[0] <= board_x and 0 < move[1] <= board_y and not is_occupied(move[1], move[0], occupied_spaces)):
            moves_list.append(move)
    return moves_list


def space_in_possible_moves(row, column, possible_moves):
    for x in possible_moves:
        if x[1] == row and x[0] == column:
            return True
    return False


def number_of_possible_moves(pos_x, pos_y, board_y, board_x, occupied_spaces):
    cnt = 0
    for row in range(board_y, 0, -1):
        for column in range(1, board_x + 1):
            if space_in_possible_moves(row, column, get_possible_moves(pos_y, pos_x, board_y, board_x, occupied_spaces)) and not is_occupied(row, column, occupied_spaces):
                cnt += 1
    return cnt


def is_occupied(pos_x, pos_y, occupied_spaces):
    for x in occupied_spaces:
        if pos_x == x[1] and pos_y == x[0]:
            return True
    return False


def get_move(board_y, board_x, possible_moves):
    cnt = 0
    while True:
        if cnt == 0:
            cnt = 1
            pos = input("Enter your next move:")
        else:
            pos = input("Invalid move! Enter your next move:")
        try:
            pos_x, pos_y = pos.split(sep=" ")
            pos_x = int(pos_x)
            pos_y = int(pos_y)
            assert pos_y in range(1, board_y + 1)
            assert pos_x in range(1, board_x + 1)
            if space_in_possible_moves(pos_y, pos_x, possible_moves):
                break
        except Exception:
            pass
    return pos_x, pos_y


# Initialize board
while True:
    board = input("Enter your board dimensions: ")
    try:
        board_x, board_y = board.split(sep=" ")
        board_y = int(board_y)
        board_x = int(board_x)
        assert board_y > 0
        assert board_x > 0
    except Exception:
        print("Invalid dimensions!")
    else:
        break


while True:
    pos = input("Enter the knight's starting position: ")
    try:
        pos_x, pos_y = pos.split(sep=" ")
        pos_x = int(pos_x)
        pos_y = int(pos_y)
        assert pos_y in range(1, board_y + 1)
        assert pos_x in range(1, board_x + 1)
    except Exception:
        print("Invalid dimensions!")
    else:
        break
# Initialize starting position

del_mult = calculate_delimiter_multiplier(board_y, board_x)
y_delimiter = calculate_delimiter(board_x)
occupied_spaces = [[pos_x, pos_y]]
possible_moves = get_possible_moves(pos_x, pos_y, board_y, board_x, occupied_spaces)
visits = 0

# while len(possible_moves) > 0:
while True:
    visits += 1
    print(get_dashes(del_mult, y_delimiter, board_x))
    for row in range(board_y, 0, -1):
        to_print = f"{get_row_prefix(row, y_delimiter)}| "
        for column in range(1, board_x + 1):
            if (pos_x == column) and (pos_y == row):
                to_print += " " * (del_mult - 1) + "X "
            elif is_occupied(row, column, occupied_spaces):
                to_print += " " * (del_mult - 1) + "* "
            elif space_in_possible_moves(row, column, possible_moves):
                to_print += " " * (del_mult - 1) + f"{number_of_possible_moves(row, column, board_y, board_x, occupied_spaces)} "
            else:
                to_print += ("_" * del_mult) + " "
        to_print += "|"
        print(to_print)
    print(get_dashes(del_mult, y_delimiter, board_x))
    print(get_footer(del_mult, y_delimiter, board_x))
    print()
    if len(possible_moves) == 0:
        break
    pos_x, pos_y = get_move(board_y, board_x, possible_moves)
    occupied_spaces.append([pos_x, pos_y])
    possible_moves = get_possible_moves(pos_x, pos_y, board_y, board_x, occupied_spaces)

if visits == (board_x * board_y):
    print("What a great tour! Congratulations!")
else:
    print("No more possible moves!")
    print(f"Your knight visited {visits} squares!")
