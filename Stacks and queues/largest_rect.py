# Imagine a number of buildings each with a width of 1 unit placed next to one another on a number line. Each building
# will have a height stated in units that match the units of the number line.
#
# Given a list of building heights in order from left to right, assuming the buildings are adjacent, calculate the largest
# rectangle you could form choosing any segment of the line of buildings. Take a look at the example problem and the
# meaning should be clear. The numbers below the number line represent the heights of the buildings.


from collections import deque


def largest_rectangle(h):
    # Complete this function
    max_area = -1
    stack_pos = deque()
    stack_h = deque()

    for i in range(len(h)):
        if len(stack_pos) < 1 or h[i] > stack_h[-1]:
            stack_pos.append(i)
            stack_h.append(h[i])
        else:
            while len(stack_pos) > 0 and h[i] < stack_h[-1]:
                tmp_post = stack_pos.pop()
                max_area = get_max_area(stack_h.pop(), i,
                                        tmp_post, max_area)

            stack_pos.append(tmp_post)
            stack_h.append(h[i])
            # if there's elements left in the stack
    while len(stack_pos) > 0 and len(stack_h) > 0:
        max_area = get_max_area(stack_h.pop(), len(h),
                                stack_pos.pop(), max_area)
    return max_area


def get_max_area(height, current_pos, rect_started, current_max):
    area = height * (current_pos - rect_started)
    return max(area, current_max)


print(largest_rectangle([8979, 4570, 6436, 5083, 7780, 3269, 5400, 7579, 2324, 2116]))
