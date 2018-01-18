from collections import deque


def is_matched(expression):
    left_symbols = '([{'
    right_symbols = ')]}'
    stack = deque()

    for char in expression:
        if char in left_symbols:
            stack.append(char)
        elif char in right_symbols:
            if len(stack) < 1:
                return False
            print(stack.pop())
            # if right_symbols.index(char) != left_symbols.index(stack.pop()):
            #     return False
    return True



stack = deque()
stack.append(1)
stack.append(4)
stack.append(10)
print(stack.popleft())


