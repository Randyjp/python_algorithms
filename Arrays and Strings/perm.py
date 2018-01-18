# 1.2) Determine if two strings are permutations


# def is_perm(str1='', str2=''):
#     if (len(str1) != len(str2)):
#         return False
#
#     if sorted(''.join(str1.lower())) == sorted(''.join(str2.lower())):
#         return True
#     return False


def is_perm(str1='', str2=''):
    if (len(str1) != len(str2)):
        return False

    chars1 = list(str1.lower())
    chars2 = list(str2.lower())
    freq = {}

    for char in chars1:
        freq[char] = 1 + freq.get(char, 0)

    for char in chars2:
        freq[char] = freq.get(char, 0) - 1

        if freq[char] < 0:
            return False

    return True

print(is_perm('mnb', 'aaa'))
