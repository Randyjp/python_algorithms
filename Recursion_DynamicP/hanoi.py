# 8.6 create a hanoi towers solver

from collections import deque


def hanoi(num_discs, origin, buffer, destination):
    if num_discs == 1:
        disc = origin.popleft()
        destination.appendleft(disc)

    elif num_discs == 2:
        hanoi(1, origin, buffer, destination)  # move one

        disc = origin.popleft()
        buffer.appendleft(disc)

        disc = destination.popleft()
        origin.appendleft(disc)

        disc = buffer.popleft()
        destination.appendleft(disc)

        hanoi(1, origin, buffer, destination)  # move one

    else:
            hanoi(num_discs-1, origin, destination, buffer)
            hanoi(1, origin, buffer, destination)
            hanoi(num_discs-1, buffer, origin, destination)




# test code:
discs = 10
tower1 = deque()
tower2 = deque()
tower3 = deque()

for i in range(discs):
    tower1.append(i)

hanoi(discs, tower1, tower2, tower3)

print(tower1)
print(tower2)
print(tower3)
