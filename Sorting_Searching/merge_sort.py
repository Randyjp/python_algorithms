def merge_sort(arr):
    arr_len = len(arr)
    if arr_len <= 0:
        return
    if arr_len == 1:
        return arr

    mid_point = arr_len // 2
    left = merge_sort(arr[0:mid_point])
    right = merge_sort(arr[mid_point:])
    return merge(left, right)


def merge(left, right):
    helper = left + right
    current = 0
    left_pointer = 0
    right_pointer = 0

    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] < right[right_pointer]:
            helper[current] = left[left_pointer]
            left_pointer += 1
        else:
            helper[current] = right[right_pointer]
            right_pointer += 1
        current += 1

    while left_pointer < len(left):
        helper[current] = left[left_pointer]
        left_pointer += 1
        current += 1

    return helper


# test code
array = [10, 5, 4, 1, 2, 3, 25]
print(merge_sort(array))
