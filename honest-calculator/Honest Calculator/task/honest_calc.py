# write your code here
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
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
        try:
            x = float(x)
            y = float(y)
        except ValueError:
            is_valid_number = False
            print(msg_1)
    if oper not in ["+", "-", "*", "/"]:
        is_valid_operator = False
        print(msg_2)
