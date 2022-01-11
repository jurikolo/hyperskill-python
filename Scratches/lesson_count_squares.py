overall_sum = 0
inputs = []
sum_of_squares = 0
while True:
    current_input = int(input())
    overall_sum += current_input
    inputs.append(current_input)
    if overall_sum == 0:
        break

if inputs[0] == 0:
    print(0)
else:
    for number in inputs:
        sum_of_squares += (number ** 2)
    print(sum_of_squares)