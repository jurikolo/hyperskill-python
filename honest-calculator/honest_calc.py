# write your code here
def check(v1, v2, v3):
    msg_6 = " ... lazy"
    msg_7 = " ... very lazy"
    msg_8 = " ... very, very lazy"
    msg_9 = "You are"
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6
    if (v1 == 1 or v2 == 1) and (v3 == "*"):
        msg += msg_7
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg += msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)


def is_one_digit(v):
    tmp = int(v)
    if (tmp == v) and (v > -10) and (v < 10):
        return True
    return False


msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

x = 0.0
y = 0.0
memory = 0.0
oper = ""
result = ""

continue_calculations = True
while continue_calculations:
    is_valid_divisor = False
    while not is_valid_divisor:
        is_valid_divisor = True
        is_valid_operator = False
        while not is_valid_operator:
            is_valid_operator = True
            is_valid_number = False
            while not is_valid_number:
                is_valid_number = True
                print(msg_0)
                calc = input()
                x, oper, y = calc.split(
                    sep=' ',
                    maxsplit=2
                )
                if x == "M":
                    x = memory
                if y == "M":
                    y = memory
                try:
                    x = float(x)
                    y = float(y)
                except ValueError:
                    is_valid_number = False
                    print(msg_1)
            if oper not in ["+", "-", "*", "/"]:
                is_valid_operator = False
                print(msg_2)
            else:
                check(x, y, oper)
                if oper == "+":
                    result = x + y
                elif oper == "-":
                    result = x - y
                elif oper == "*":
                    result = x * y
                elif y == 0:
                    is_valid_divisor = False
                    print(msg_3)
                else:
                    result = x / y
    print(result)
    answer_4 = ""
    while answer_4 not in ["y", "n"]:
        print(msg_4)
        answer_4 = input()
    if answer_4 == "y":
        if is_one_digit(result):
            msg_index = 10
            answer_10 = ""
            ask_stupid_question = True
            while ask_stupid_question:
                while (answer_10 not in ["y", "n"]) or (answer_10 == "y" and msg_index < 13):
                    if answer_10 == "y":
                        msg_index += 1
                    if msg_index == 10:
                        print(msg_10)
                        answer_10 = input()
                    elif msg_index == 11:
                        print(msg_11)
                        answer_10 = input()
                    elif msg_index == 12:
                        print(msg_12)
                        answer_10 = input()
                    else:
                        ask_stupid_question = False
                        memory = result
                if answer_10 == "n":
                    ask_stupid_question = False
        else:
            memory = result
    answer_5 = ""
    while answer_5 not in ["y", "n"]:
        print(msg_5)
        answer_5 = input()
    if answer_5 == "n":
        continue_calculations = False
