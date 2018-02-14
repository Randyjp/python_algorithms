# Given a collection of intervals, merge all overlapping intervals.

def mergeInt(intervals):
    if len(intervals) < 2:
        return intervals

    intervals.sort()
    pointer_1 = 0
    pointer_2 = 1

    while pointer_1 < len(intervals) and pointer_2 < len(intervals):
        interval_1 = intervals[pointer_1]
        interval_2 = intervals[pointer_2]

        if interval_1[0] <= interval_2[0] <= interval_1[1]:
            a = min(interval_1[0], interval_2[0])
            b = max(interval_1[1], interval_2[1])
            new_interval = (a, b)

            intervals[pointer_2] = new_interval
            intervals.pop(pointer_1)
        else:
            pointer_1 += 1
            pointer_2 += 1
    return intervals


A = [(4, 100), (48, 94), (16, 21), (58, 71), (36, 53), (49, 68), (18, 42), (37, 90), (68, 75), (6, 57), (25, 78),
     (58, 79), (18, 29), (69, 94), (5, 31), (10, 87), (21, 35), (1, 32), (7, 24), (17, 85), (30, 95), (5, 63),
     (1, 17), (67, 100), (53, 55), (30, 63), (7, 76), (33, 51), (62, 68), (78, 83), (12, 24), (31, 73), (64, 74),
     (33, 40), (51, 63), (17, 31), (14, 29), (9, 15), (39, 70), (13, 67), (27, 100), (10, 71), (18, 47), (48, 79),
     (70, 73), (44, 59), (68, 78), (24, 67), (32, 70), (29, 94), (45, 90), (10, 76), (12, 28), (31, 78), (9, 44),
     (29, 83), (21, 35), (46, 93), (66, 83), (21, 72), (29, 37), (6, 11), (56, 87), (10, 26), (11, 12), (15, 88),
     (3, 13), (56, 70), (40, 73), (25, 62), (63, 73), (47, 74), (8, 36)]

print(mergeInt(A))
