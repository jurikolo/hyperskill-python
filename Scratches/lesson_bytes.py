first_bytes = b'123'
print(first_bytes)  # b'123'
print(len(first_bytes))  # 3
print(first_bytes[1])  # 50, e.g. unicode symbol

print(ord("2"))  # 50, convert a Unicode character to its respective code point
print(chr(50))  # 2, converts an integer, representing a code point in the Unicode table, to the respective character

print(bytes([126]))
print("=====")
print("=====")
never_bites = b'corgi'

# 1
print(never_bites)

# 2
print(never_bites[0] + never_bites[1] + never_bites[2] + never_bites[3] + never_bites[4])
print("=====")
chinese_hello = '你好，世界'.encode()
print(chinese_hello)
print("=====")
first_number = (100).to_bytes(1, byteorder='little')
print(first_number)  # b'd'

second_number = (1024).to_bytes(2, byteorder='little')
print(second_number)  # b'\x00\x04'

third_number = (1024).to_bytes(2, byteorder='big')
print(third_number)  # b'\x04\x00'

print(f"Correct conversion back to INT: {int.from_bytes(third_number, 'big')}")
print(f"Wrong conversion back to INT: {int.from_bytes(third_number, 'little')}")

print("=====")
my_number = 12345
my_number_in_bytes = my_number.to_bytes(2, byteorder="little")
result = 0
for x in my_number_in_bytes:
    result += int(x)
print(result)

# Let's decipher a little message.
# The first input line is an encoded message, and the second line is the key integer number.
# Convert the key to two bytes and sum up its items.
# Then add the resulting sum to the code point of each character in the message. Finally, print the decoded message.
# Input:
# HlAdghmcXnt
# 256
# Result: ImBehindYou
print("=====")
print("=====")
a = "HlAdghmcXnt"
b = 256
b_bytes = b.to_bytes(2, "little")
b_sum = 0
for x in b_bytes:
    b_sum += int(x)
result = ""
for x in a:
    my_char_byte = ord(x)
    result += chr(my_char_byte + b_sum)
print(result)
print("=====")
print("=====")
a = 3
x = bytes(a)
print(x)