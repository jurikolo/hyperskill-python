first_names = ['John', 'Anna', 'Tom']
last_names = ['Smith', 'Williams', 'Davis']

for name, last_name in zip(first_names, last_names):
    print(name, last_name)

print("=====")
print("=====")
months_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
               'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

for n, month in enumerate(months_list):
    print(n + 1, month)

print("=====")
print("=====")
short_list = [1, 2, 3]
long_list = [10, 20, 30, 40]

for a, b in zip(short_list, long_list):
    print(a, b)

print("=====")
print("=====")
# for a, b in zip(short_list, long_list, strict=True):  # added strict condition, new in Python 3.10
#     print(a, b)

# task 1, search for combination of main, drink and dessert not over 30$
main_courses = ['beef stew', 'fried fish']
price_main_courses = [28, 23]

desserts = ['ice-cream', 'cake']
price_desserts = [2, 4]

drinks = ['cola', 'wine']
price_drinks = [3, 10]

import itertools
for main, dessert, drink in itertools.product(zip(main_courses, price_main_courses), zip(desserts, price_desserts), zip(drinks, price_drinks)):
    if main[1] + dessert[1] + drink[1] <= 30:
        print(main[0], dessert[0], drink[0], main[1] + dessert[1] + drink[1])

print("=====")
print("=====")
teams = ['Best-ever', 'Not-so-good', 'Amateurs']
my_iter = itertools.combinations(iterable=teams, r=2)
try:
    while True:
        print(next(my_iter))
except StopIteration:
    pass