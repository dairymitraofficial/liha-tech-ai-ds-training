physics = int(input("Enter Physics marks: "))
chemistry = int(input("Enter Chemistry marks: "))
biology = int(input("Enter Biology marks: "))
mathematics = int(input("Enter Mathematics marks: "))
computer = int(input("Enter Computer marks: "))

total = physics + chemistry + biology + mathematics + computer

per = (total / 500) * 100

print("Percentage =", per)

if per >= 0 and per <= 100:

    if per >= 90:
        print("Grade = A")

    elif per >= 80:
        print("Grade = B")

    elif per >= 70:
        print("Grade = C")

    elif per >= 60:
        print("Grade = D")

    elif per >= 40:
        print("Grade = E")

    else:
        print("Grade = F")

else:
    print("Please enter valid marks")