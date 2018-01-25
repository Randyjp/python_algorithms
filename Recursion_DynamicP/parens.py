# 8.9) Print all valid combinations of n pairs of parenthesis

# solution #1

def paren(n):
    if n == 1:
        return ['()']

    combs = paren(n - 1)
    res = []

    for s in combs:
        for i in range(len(s)):
            s_list = list(s)
            s_list.insert(i, ')')
            s_list.insert(i, '(')
            res.append(''.join(s_list))

    return set(res)


# solution #2
def parens(right, left, string, result):
    if left < 0 or left > right:
        return

    if right == 0 and left == 0:
        result.append(string)
    else:
        if left > 0:
            string += '('
            parens(right, left - 1, string, result)
        if right > left:
            string += ')'
            parens(right - 1, left, string, result)


# test code
res = []
parens(2, 2, '', res)
print(res)
