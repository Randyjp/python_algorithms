#  3.5) keep a sorted stack


from ArrayStack import ArrayStack
from Empty import Empty

class SortedStack:
    def __init__(self):
        self._stack = ArrayStack()

    def peek(self):
        return self._stack.peek()

    def pop(self):
        return self._stack.pop()

    def push(self, value):
        temp = ArrayStack()

        if self._stack.is_empty() or self._stack.peek() > value:
            self._stack.push(value)
        else:
            hold = value
            size = len(self._stack) + 1

            while len(self._stack) != size:
                if self.peek() < hold and self.peek() is not None:
                    temp.push(self.pop())
                elif hold is not None:
                    self._stack.push(hold)
                    hold = None
                else:
                    self._stack.push(temp.pop())

# test code

stack = SortedStack()
stack.push(4)
stack.push(2)
stack.push(3)
stack.push(10)
stack.push(120)
stack.push(1)

print(stack.pop())
print(stack.pop())
