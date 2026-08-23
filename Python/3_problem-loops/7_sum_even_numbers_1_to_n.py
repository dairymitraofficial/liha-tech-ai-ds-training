n = int(input("Enter n- "))

sum = 0
i = 1
while i<=n:
    if i%2==0:
        sum += i
    i+=1
print("Sum = ",sum)
