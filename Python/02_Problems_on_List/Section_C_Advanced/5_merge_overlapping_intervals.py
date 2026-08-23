intervals = [[1, 3], [2, 6], [8, 10], [9, 12]]

intervals.sort()

result = []

for interval in intervals:

    if len(result) == 0:
        result.append(interval)

    else:
        last = result[-1]

        if interval[0] <= last[1]:

            if interval[1] > last[1]:
                last[1] = interval[1]

        else:
            result.append(interval)

print("Merged intervals =", result)