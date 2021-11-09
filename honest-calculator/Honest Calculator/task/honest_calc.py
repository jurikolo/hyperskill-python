# write your code here
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"

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
            elif oper == "+":
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
        memory = result
    answer_5 = ""
    while answer_5 not in ["y", "n"]:
        print(msg_5)
        answer_5 = input()
    if answer_5 == "n":
        continue_calculations = False