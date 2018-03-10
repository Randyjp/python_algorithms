class MinHeap:
    def __init__(self, heap, heap_size=None):
        self.heap = heap
        self.heap_size = heap_size if heap_size else len(heap)
        self.build()

    def __len__(self):
        # Number of elements in the queue.
        return self.heap_size

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
        left_child = self.left(index)
        right_child = self.right(index)
        smallest = index

        if left_child and self.heap[smallest - 1] > self.heap[left_child - 1]:
            smallest = left_child
        if right_child and self.heap[smallest - 1] > self.heap[right_child - 1]:
            smallest = right_child

        if smallest != index:
            temp = self.heap[index - 1]
            self.heap[index - 1] = self.heap[smallest - 1]
            self.heap[smallest - 1] = temp
            self.min_heapify(smallest)

    def build(self):
        mid = self.heap_size // 2

        for index in range(1, mid + 1):
            self.min_heapify(index)


class PriorityQueue(MinHeap):
    """Array-based priority queue implementation."""

    def __init__(self):
        """Initially empty priority queue."""
        super().__init__([])

    def append(self, key):
        """Inserts an element in the priority queue."""
        if key is None:
            raise ValueError('Cannot insert None in the queue')
        self.heap.append(key)
        self.heap_size += 1
        self.min_heapify(self.heap_size)

    def min(self):
        """The smallest element in the queue."""
        if len(self) == 0:
            return None
        return self.heap[0]

    def pop(self):
        """Removes the minimum element in the queue.

        Returns:
            The value of the removed element.
        """
        if len(self) == 0:
            return None
        popped_key = self.heap.pop(0)
        self.heap_size -= 1
        self.min_heapify(0)
        return popped_key
