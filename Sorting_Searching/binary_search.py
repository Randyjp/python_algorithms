def binary_search(arr, num):
    if len(arr) < 1:
        return -1  # error
    mid_index = int(len(arr) / 2)
    mid_point = arr[mid_index]

    if mid_point == num:
        return num
    elif mid_point > num:
        return binary_search(arr[0:mid_index], num)
    else:
        return binary_search(arr[mid_index + 1:], num)


# test code
arr = [2, 5, 20, 25, 30, 100, 1000, 10002]
print(binary_search(arr, 30))
