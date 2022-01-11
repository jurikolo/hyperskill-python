def xor(a, b):
    # Write your code here
    if bool(a) and bool(b):
        return False
    if not bool(a) and not bool(b):
        return False
    return True


print(xor(1, 2))
print(xor(0, False))
print(xor(True, False))
print(xor(False, True))
print(xor(1, False))
print(xor(1, True))
