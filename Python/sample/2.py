l = [1, 2, 3, 4, 6]
n = 6

actual_sum = n*(n+1)//2
total_sum = 0

for i in l:
    total_sum  += i

missimg = actual_sum - total_sum

print("missing= ", missimg)