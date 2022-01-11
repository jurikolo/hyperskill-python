import math

def solve_it(x, y):
    return math.sqrt((math.pi - x) ** 2 + (math.e - y) ** 2) <= math.sqrt(2)


print(solve_it(4, 2))
print(solve_it(3, 2))
print(solve_it(2, 2))
print(solve_it(3, 4))
print(solve_it(4, 4))
print(solve_it(2, 4))

