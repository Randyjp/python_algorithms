from Empty import Empty


class ArrayQueue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._front = 0
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('The queue is empty')
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise Empty('The queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % self._size
        self._size -= 1
        if 0 < self.size < len(self.data) // 4: 
            self.resize(len(self.data) // 2)
        return answer

    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(self._size * 2)
        avail = (self.front + self.size) % len(self.data)
        self.data[avail] = e
        self.size += 1

    def _resize(self, new_size):
        old = self._data
        self._data = [None] * new_size
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + self._data) % len(old)
        self._front = 0
