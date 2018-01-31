#  triangle = (0.5 * base * height), rectangle = (width * height), Circle= (PI * radius ^ 2)
import math
def triangle(base,height):
    area = .5 * base * height
    return(area)


def rectangle(width,height):
    area = width * height
    return(area)


def circle(radius):
    area = math.pi * radius ** 2
    return(area)

def square(t):
    area = t** 2
    return(area)

print(triangle(3,2))
print(rectangle(2,3))
print(circle(5))
print(square(4))
