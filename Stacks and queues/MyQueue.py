# 3.4)

from ArrayStack import ArrayStack
from Empty import Empty


class MyQueue:
    def __init__(self):
        self._stack = ArrayStack()
        self._inverted = False
        self._size = 0

    def peek(self):
        # stack = self._stack
        if self._stack.is_empty():
            raise Empty('Stack is empty')
        if not self._inverted:
            self.invert_stack()
        return self._stack.peek()

    def push(self, value):
        if self._inverted:
            self.invert_stack()
        self._stack.push(value)

    def pop(self):
        if self._stack.is_empty():
            raise Empty('Empty stack')
        if not self._inverted:
            self.invert_stack()
        return self._stack.pop()

    def invert_stack(self):
        temp = ArrayStack()
        self._inverted = not self._inverted

        while self._stack.peek() is not None:
            temp.push(self._stack.pop())
        self._stack = temp

# test code


queue = MyQueue()
queue.push(5)
queue.push(1)
queue.push(2)
queue.push(3)
queue.push(4)

print(queue.peek())
print(queue.peek())
print(queue.pop())
print(queue.pop())