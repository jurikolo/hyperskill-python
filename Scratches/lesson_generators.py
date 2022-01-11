def multiples(a, n):
    i = 1
    while i <= n:
        yield a*i
        i += 1


# This is a generator
multiples_of_three = multiples(3, 5)

# It produces the first 5 multiples of 3 one by one:
print(next(multiples_of_three))
print(next(multiples_of_three))
print(next(multiples_of_three))
print(next(multiples_of_three))
print(next(multiples_of_three))
# print(next(multiples_of_three))  # Error StopIteration will be returned

# ANOTHER WAY TO DEFINE GENERATOR
numbers = [1, 2, 3]
my_generator = (n ** 2 for n in numbers)

for n in my_generator:
    print(n)


# task 1
# n = int(input())
#
# def even(n):
#     cnt = 0
#     while True:
#         if cnt % 2 == 0:
#             cnt += 1
#             yield cnt - 1
#         else:
#             cnt += 1
#
#
# even_calc = even(n)
# for x in range(1, n + 1):
#     print(next(even_calc))

# Another solution for task 1
# def even():
#     yield from (i * 2 for i in range(n))
#
# print(*even(), sep='\n')

# task 2
# user_input = input()
# input_calculator = (int(x) for x in user_input)
# result = 0
# for a in input_calculator:
#     result += a
# print(result)

# task 3, produce an infinite sequence of the squares of all natural numbers
# user_input = int(input())
# square_calculator = (pow(x, 2) for x in range(1, user_input + 1))
# for cnt in square_calculator:
#     print(cnt)

# def squares(n):
#     num = 1
#     while num < n:
#         yield pow(num, 2)
#         num += 1
#
#
# n = int(input())
# squares_calc = squares(n + 1)
# for x in range(1, n + 1):
#     print(next(squares_calc))

# task 4, Fibonacci
print("=====")
print("=====")
def fibonacci(n):
    cnt = 1
    if cnt == 1:
        cnt += 1
        yield 0
    if cnt == 2:
        cnt += 1
        yield 1
    number1 = 0
    number2 = 1
    while cnt <= n:
        tmp = number1
        number1 = number2
        number2 += tmp
        cnt += 1
        yield number2

f_calc = fibonacci(5)
print(next(f_calc))
print(next(f_calc))
print(next(f_calc))
print(next(f_calc))
print(next(f_calc))