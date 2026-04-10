
import pdb
import math
def calculate_area (radius):

    pi = 3.14
    return pi * radius ** 2

def calculate_circumference (radius):
    pi = 3.14

    return pi* radius **2
def main():
    radius  = 5

    area = calculate_area(radius)

    import pdb; pdb.set_trace()

    circumference = calculate_circumference (radius)

    print(f"Area: {area}")

    print(f"circumference: {circumference}")

main()

import math

def circle_calculation(radius):

    area = math.pi*radius*radius

    circumference =math.pi*radius

    return area, circumference

radius = float(input("Enetr radius:"))

a,c=circle_calculation(radius)

print("area of circle:",a)

print("circumference of circle:",c)
