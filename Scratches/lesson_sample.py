def last_indexof_max(numbers):
    if not numbers:
        return -1
    result = 0
    for cnt in range(1, len(numbers)):
        if numbers[cnt] >= numbers[result]:
            result = cnt
    return result


input_numbers = [8, 11, 15, 15, 15, 12]
print(last_indexof_max(input_numbers))
print("=====")
print("=====")
salary = "11\n22\n33\n"
salary_2 = salary.split("\n")
print(salary_2)
for x in salary_2:
    if x != "":
        print(int(x) * 12)

print("=====")
print("=====")
