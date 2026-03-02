#task1
import math

degree = float(input("Input degree: "))

radian = math.radians(degree)

print("Output radian:", round(radian, 6))

#task2
height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))

area = (base1 + base2) / 2 * height

print("Expected Output:", area)

#task3
import math

n = int(input("Input number of sides: "))
a = float(input("Input the length of a side: "))

area = (n * a ** 2) / (4 * math.tan(math.pi / n))

print("The area of the polygon is:", int(area))

#task4
base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))

area = base * height

print("Expected Output:", area)