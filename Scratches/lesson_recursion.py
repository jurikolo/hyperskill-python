# frogs
# def number_of_frogs(year):
#     if year == 1:
#         return 120
#     else:
#         return 2 * (number_of_frogs(year - 1) - 50)
#
#
# print(number_of_frogs(5))

# sum of natural numbers
# def rec_sum(n):
#     if n == 1:
#         return 1
#     else:
#         return n + rec_sum(n - 1)
#
# print(rec_sum(3))

# multiply with sum
# def multiply(a, b):
#     # base case
#     if b == 1:
#         return a
#     # recursive case
#     return a + multiply(a, b - 1)
#
# print(multiply(2, 5))

# Fibonacci numbers
def fib(n):

    # base case n = 0
    if n == 0:
        return 0
        # base case n = 1
    elif n == 1:
        return 1
        # case n > 1
    else:
        return fib(n - 1) + fib(n - 2)

print(fib(5))