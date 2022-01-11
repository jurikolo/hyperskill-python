# import the required library
from math import cos, radians

def calculate_cosine(angle_in_degrees):
    # do not forget to round the result and print it
    angle_in_radians = radians(angle_in_degrees)
    print(round(cos(angle_in_radians), 2))

x = int(input())
calculate_cosine(x)