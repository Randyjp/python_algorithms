# 8.5) create a function to multiply two numbers without using *

def recursive_multiply(num1, num2):
    if num1 > num2:
        return multiply(num1, num2)
    else:
        return multiply(num2, num1)


def multiply(num1, num2):
    if num2 == 0:
        return 0
    elif num2 == 1:
        return num1

    half_point = num2 >> 1 # divide by two
    half_mult = multiply(num1, half_point)

    if num2 % 2 == 0:
        return half_mult + half_mult
    else:
        return half_mult + half_mult + num1


# test code

# print(10 >> 2)
print(recursive_multiply(5, 100))
