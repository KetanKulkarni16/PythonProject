#This program is about finding the roots of quadratic equation

import math

a = 1
b = -5
c = 6


r1 = (-b + math.sqrt(b**2 - 4 * a * c)) / ( 2 * a)

r2 = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)

print('Root 1: ', r1)
print('Root 2: ', r2)
