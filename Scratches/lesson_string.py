# email = "asdf@ggggg.com"
# print(email.split(sep="@")[0])

# word = "asdf"
# index = word.find("q")
# print(index)

# Print only characters in odd places
my_string = "qwerty"
cnt = 1
result = ""
for x in my_string:
    if cnt % 2 == 0:
        result += x
    cnt += 1
print(result)

# Another solution
print("".join([my_string[x] for x in range(len(my_string)) if x % 2 == 1]))

# Another solution
print(my_string[1::2])