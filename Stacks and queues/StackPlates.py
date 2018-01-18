# 3.3)
from Empty import Empty


class SetOfStacks:
    def __init__(self, cap):
        self._data = []
        stack = [None] * cap
        self._data.append(stack)
        self._last = -1
        self._cap = cap

    def _get_current_stack(self):
        if len(self._data) < 1:
            raise Empty('No stacks')
        return self._data[-1]

    def pop(self):
        stack = self._get_current_stack()
        last = self._last
        value = stack[last]
        new_last = self._last - 1

        if value is None:
            raise Empty('The stack is empty')

        if last == 0 and stack[new_last] is None:
            self._data.pop()
            self._last = self._cap - 1

        else:
            stack[last] = None
            self._last = new_last

        return value

    def push(self, value):
        if (self._last + 1) == self._cap:
            stack = [None] * self._cap
            self._last = 0
            stack[0] = value
            self._data.append(stack)

        else:
            stack = self._get_current_stack()
            index = (1 + self._last) % self._cap
            stack[index] = value
            self._last += 1


#test code

stacks = SetOfStacks(5)
stacks.push(1)
stacks.push(2)
stacks.push(3)
stacks.push(4)
stacks.push(5)

stacks.push(6)
stacks.push(7)
stacks.push(8)
stacks.push(9)
stacks.push(10)

stacks.push(11)

stacks.pop()
stacks.pop()
stacks.pop()
stacks.pop()
stacks.pop()
stacks.pop()
stacks.pop()
stacks.pop()
stacks.pop()
stacks.pop()
stacks.pop()

stacks.push(1)
stacks.push(2)
stacks.push(3)
stacks.push(4)
stacks.push(5)

stacks.push(6)
stacks.push(7)
stacks.push(8)
stacks.push(9)
stacks.push(10)

stacks.push(11)

print(stacks)

