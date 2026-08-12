bs = int(input("Enter a Basic Salary: "))

if bs <= 10000:
    hra = bs * 0.20
    da = bs * 0.80
    gs = bs + hra + da
    print("HRA =", hra)
    print("DA =", da)
    print("Gross Salary =", gs)

elif bs <= 20000:
    hra = bs * 0.30
    da = bs * 0.90
    gs = bs + hra + da
    print("HRA =", hra)
    print("DA =", da)
    print("Gross Salary =", gs)

else:
    hra = bs * 0.35
    da = bs * 0.95
    gs = bs + hra + da
    print("HRA =", hra)
    print("DA =", da)
    print("Gross Salary =", gs)