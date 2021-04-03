# scalene triangle: all sides have different lenghts
# Isosceles triangle: Two sides have the same length
# Equilateral triangle: all sides are equal

a = int(input("the lenght of side a = "))
b = int(input("the lenght of side b = "))
c = int(input("the lenght of side c = "))

if a!= b and b != c and a != c:
    print("This is a scalene triangle")
elif a == b and b == c:
    print("This is an equilateral triangle")
else:
    print("This is an isosceles triangle")