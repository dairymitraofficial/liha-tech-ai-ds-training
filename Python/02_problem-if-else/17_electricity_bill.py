units = int(input("Enter electricity units: "))

if units > 0 and units <= 50:
    bill = units * 0.50

elif units <= 150:
    bill = (50 * 0.50) + ((units - 50) * 0.75)

elif units <= 250:
    bill = (50 * 0.50) + (100 * 0.75) + ((units - 150) * 1.25)

elif units > 250:
    bill = (50 * 0.50) + (100 * 0.75) + (100 * 1.25) + ((units - 250) * 1.50)

else:
    print("Enter valid units")
    exit()

surcharge = bill * 0.17
total_bill = bill + surcharge

print("Bill =", round(bill, 2))
print("Surcharge =", round(surcharge, 2))
print("Total Bill =", round(total_bill, 2))