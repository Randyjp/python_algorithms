# 8.1) A child can take 1,2 or 3 hops in a staircase of n steps. Given n, how many possible ways the child can
# up the stairs?


cache = {}


def steps(n):
    if n < 0:
        return 0
    if n == 1:
        return n

    if not cache.get(n, False):
        cache[n] = steps(n - 3) + steps(n - 2) + steps(n -1)

    return cache[n]



# test code
print(steps(37))
