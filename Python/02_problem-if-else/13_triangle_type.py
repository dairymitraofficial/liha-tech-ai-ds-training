side1 = int(input("Enter first side: "))
side2 = int(input("Enter second side: "))
side3 = int(input("Enter third side: "))

if side1 == side2 and side2 == side3:
    print("Equilateral Triangle")

elif side1 != side2 and side2 != side3 and side1 != side3:
    print("Scalene Triangle")

else:
    print("Isosceles Triangle")
