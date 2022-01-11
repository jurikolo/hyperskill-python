try:
    2 / 0
except Exception:
    print("except Exception")
except ZeroDivisionError:
    print("except ZeroDivisionError")
except ArithmeticError:
    print("except ArithmeticError")
finally:
    print("finally")


def my_func():
    try:
        1/0
    except:
        1/0
    finally:
        return "It's OK."

print(my_func())
print("#####")
print("#####")
try:
    a = int("5")
except ZeroDivisionError:
    print("except ZeroDivisionError")
else:
    print("In else block")
finally:
    print("The end")

print("#####")
print("#####")
x = 4
y = 2
assert (x ** 2 / y ** 2) - y != 2, "There are wrong values!"
print(x, y)
