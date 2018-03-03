from heaps.max_heap import MaxHeap


def heap_sort(arr):
    max_heap = MaxHeap(arr)

    for i in range(max_heap.heap_size, 1, -1):
        temp = max_heap.heap[i - 1]
        max_heap.heap[i - 1] = max_heap.heap[0]
        max_heap.heap[0] = temp
        max_heap.heap_size -= 1
        max_heap.max_heapify(1)
    return max_heap.heap


unsorted = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
print(heap_sort(unsorted))
