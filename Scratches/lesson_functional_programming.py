def celsius_to_fahrenheit(c):
    return ((c + 40) * 1.8) - 40


scores_maths = [100, 75, 90, 95, 60, 50, 95, 85, 70, 75,
                90, 85, 60, 45, 100, 70, 65, 50, 55, 95,
                50, 45, 35, 100, 95, 90, 85, 90, 80, 85,
                95, 45, 60, 45, 80, 70, 55, 45, 60, 90]

scores_physics = [50, 65, 85, 100, 60, 55, 90, 85, 70, 90,
                  50, 40, 100, 45, 95, 70, 75, 60, 50, 100,
                  60, 90, 40, 90, 95, 90, 80, 95, 85, 80,
                  95, 90, 75, 50, 80, 70, 50, 35, 65, 90]

scores_english = [50, 40, 100, 45, 95, 70, 75, 60, 50, 100,
                  50, 45, 35, 100, 95, 90, 85, 90, 80, 85,
                  90, 85, 60, 45, 100, 70, 65, 50, 55, 95,
                  50, 65, 85, 100, 60, 55, 90, 85, 70, 90]

overall_scores = list(map(lambda x, y, z: x + y + z, scores_maths, scores_physics, scores_english))

admitted_students = list(filter(lambda x: x >= 270, overall_scores))

print(len(admitted_students))

print("=====")
print("=====")
even = [0, 2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

my_sum = list(map(lambda x, y: x + y, even, odd))

remainders = list(map(lambda x: x % 3, my_sum))

nonzero_remainders = list(filter(lambda r: r, remainders))

print(my_sum)
print(remainders)
print(nonzero_remainders)

print("=====")
print("=====")
daily_temp_c = [20.5, 19, 15, 25, 27, 30, 31, 29, 26, 21,
                19, 25, 27.5, 28, 26, 29.5, 31, 27.5, 26, 29,
                18, 17.5, 17, 16.5, 19, 20, 25, 26.5, 27, 28,
                20.5, 19, 25, 27.5, 28, 26, 15, 25, 27, 28]

daily_temp_f = list(map(celsius_to_fahrenheit, daily_temp_c))

temp_above_80 = list(filter(lambda x: x > 80, daily_temp_f))

print(len(temp_above_80))
