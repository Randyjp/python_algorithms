def counting_sort(arr, max_value):
    m = max_value + 1
    count = [0] * m

    for x in arr:
        count[x] += 1

    current = 0
    for x in range(m):  # for each counted value
        for j in range(count[x]):  # for as many time as that value was counted
            arr[current] = x
            current += 1
    return arr


# test code
# array = [10, 5, 4, 1, 2, 3, 25, 25, 25]
# print(counting_sort(array, 25))
