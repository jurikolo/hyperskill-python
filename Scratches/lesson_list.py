def my_func(x):
    global my_global_var
    my_global_var += int(x)
    return my_global_var


my_list = [x for x in range(1,1000) if x % 3 == 0]
print(my_list)

# [1, 2, 3] to [1, 1 + 2, 1 + 2 + 3], which equals to [1, 3, 6].

print()
print()
user_input = "123"
my_global_var = 0
# user_input = input()
old_int_list = [my_func(x) for x in user_input]
print(old_int_list)

print()
print()
lists = [0, [1, [2, 3]]]
print(lists[1][1][0])

print()
print()
user_input = "123"
# user_input = input()
user_list = [int(x) for x in user_input]
user_list2 = []
for cnt in range(len(user_list)):
    if cnt != 0:
        user_list2.append((user_list[cnt] + user_list[cnt - 1]) / 2)
    print(cnt)
print(user_list2)
print("=====")
print("=====")
# amount_of_games = int(input())
# user_input = []
# for cnt in range(amount_of_games):
#     user_input.append(input())
# winners = []
# for x in user_input:
#     record = x.split(' ')
#     print(record)
#     if (record[1] == "win"):
#         winners.append(record[0])

text = [["Glitch", "is", "a", "minor", "problem", "that", "causes", "a", "temporary", "setback"],
        ["Ephemeral", "lasts", "one", "day", "only"],
        ["Accolade", "is", "an", "expression", "of", "praise"]]
length = int(input())
print([ x for row in text for x in row if len(x) <= length])