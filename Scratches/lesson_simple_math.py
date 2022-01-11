def is_leap(year):
    if year % 400 == 0:
        print("Divides by 400")
        return True
    if year % 100 == 0:
        print("Divides by 100")
        return False
    if year % 4 == 0:
        print("Divides by 4")
        return True
    else:
        print("Doesn't divide at all, lol")
        return False


x = 2100
is_leap(x)