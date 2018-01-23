# 8.3) given an array of distinct integers write a method to find a magic index. magic index -> A[i] = i


def magic(arr):
    n = len(arr)
    if n == 0:
        return None
    return magic_binary(arr, 0, n-1)
    # return magic_index(arr, n, 0)


def magic_index(arr, n, i):
    if i >= n:
        return None
    value = arr[i]
    if value == i:
        return i
    else:
        return magic_index(arr, n, value)


def magic_binary(arr, start, end):
    if end < start:
        return None

    mid_index = int((start + end) / 2)
    mid_value = arr[mid_index]

    if mid_value == mid_index:
        return mid_index

    # search left
    left_index = min(mid_index - 1, mid_value)
    left = magic_binary(array, start, left_index)
    if left:
        return left
    # search right
    right_index = max(mid_index + 1, mid_value)
    right = magic_binary(array, right_index, end)
    if right:
        return right


# test code
array = [1, 2, 3, 3, 4, 5, 5]
print(magic(array))
