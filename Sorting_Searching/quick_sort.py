from random import randint


def quick_sort(arr, left, right):
    if left >= right:
        return
    pivot_index = partition(arr, left, right)  # partition the array.
    quick_sort(arr, left, pivot_index - 1)  # sort left side
    quick_sort(arr, pivot_index, right)  # sort right side


def partition(arr, left, right):
    index = randint(left, right)  # random index for partition
    pivot = arr[index]

    while left <= right:
        while arr[left] < pivot: # find elements to left that are > that pivot
            left += 1
        while arr[right] > pivot: # find elements to right that are < that pivot
            right -= 1

        if left <= right:
            # swap numbers
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp
            left += 1
            right -= 1

    return left  # return the partition point


# test code
array = [10, 5, 4, 1, 2, 3, 25]
quick_sort(array, 0, len(array) - 1)
print(array)
