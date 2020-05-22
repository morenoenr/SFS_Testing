from math import pi

print("This is my first test in pyhton!")

#Calculates the area of a circle given the radius
def circle_area(r):
    if type(r) not in [int, float]:
        raise ValueError("The radius must be a number.")
    if r < 0:
        raise ValueError("The radius cannot be negative.")
    return pi*(r**2)
