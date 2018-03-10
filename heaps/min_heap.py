class MinHeap:
    def __init__(self, heap, heap_size=None):
        self.heap = heap
        self.heap_size = heap_size if heap_size else len(heap)
        self.build()

    def left(self, index):
        left_index = 2 * index
        if left_index > self.heap_size:
            return None
        return left_index

    def right(self, index):
        right_index = (2 * index) + 1
        if right_index > self.heap_size:
            return None
        return right_index

    def min_heapify(self, index):
        left_child = self.left(index) - 1
        right_child = self.right(index) - 1
        smallest = index - 1

        if smallest is not None and self.heap[smallest] > self.heap[left_child]:
            smallest = left_child
        if smallest is not None and self.heap[smallest] > self.heap[right_child]:
            smallest = right_child

        if (smallest + 1) != index:
            temp = self.heap[index - 1]
            self.heap[index - 1] = self.heap[smallest]
            self.heap[smallest] = temp
            self.min_heapify(smallest + 1)

    def build(self):
        mid = self.heap_size // 2

        for index in range(1, mid + 1):
            self.min_heapify(index)


# test code
non_min_heap = [4, 1, 3, 2, 9, 10, 14, 8, 7]
max_heap = MinHeap(non_min_heap)
print(max_heap.heap)
