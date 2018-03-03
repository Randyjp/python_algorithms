class MaxHeap:
    def __init__(self, heap, heap_size=None):
        self.heap = heap
        self.heap_size = heap_size if heap_size else len(heap)
        self.build()

    def left(self, i):
        left_index = 2 * i
        if left_index > self.heap_size:
            return None
        return left_index

    def right(self, i):
        right_index = (2 * i) + 1
        if right_index > self.heap_size:
            return None
        return right_index

    def max_heapify(self, i):
        left_child = self.left(i)
        right_child = self.right(i)
        largest = i

        if left_child and self.heap[left_child-1] > self.heap[largest-1]:
            largest = left_child
        if right_child and self.heap[right_child-1] > self.heap[largest-1]:
            largest = right_child

        if largest != i:
            temp = self.heap[i-1]
            self.heap[i-1] = self.heap[largest-1]
            self.heap[largest-1] = temp
            self.max_heapify(largest)

    def build(self):
        mid = (self.heap_size // 2)
        for i in range(mid, 0, -1):
            self.max_heapify(i)


# test code
non_max_heap = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
max_heap = MaxHeap(non_max_heap)
print(max_heap.heap)
