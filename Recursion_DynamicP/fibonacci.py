# normal recursive implementation :(

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# print(fibonacci(40))

# top-down dynamic programming or memoization
cached = {}

def fibonacci_top(n):
    if n == 0 or n == 1:
        return n
    if not cached.get(n, False):
        cached[n] = fibonacci_top(n - 1) + fibonacci_top(n - 2)

    return cached[n]


# bottom-down dynamic programming or memoization

def fibonacci_bottom(n):
    if n == 0:
        return n
    a = 0
    b = 1
    for x in range(n):
        c = a + b

        a = b
        b = c

    return a + b

print(fibonacci_bottom(10000))

