num1 = int(input("Enter First number- "))
num2 = int(input("Enter Second number- "))
num3 = int(input("Enter Third number- "))

if num1>num2 and num1>num3:
    print(num1, " is Maximum")
elif num1<num2 and num3<num2:
    print(num2, " is Maximum")
else:
    print(num3, " is Maximum")