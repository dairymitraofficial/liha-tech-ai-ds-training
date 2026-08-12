CP = int(input("Enter a Cost Price (CP)- "))
SP = int(input("Enter a Selling Price (SP)- "))

cost = SP - CP

if cost > 0:
    print("Profit = ",cost)

elif cost < 0:
    print("Loss = ",-(cost))

else:
    print("No Profit No Loss")

