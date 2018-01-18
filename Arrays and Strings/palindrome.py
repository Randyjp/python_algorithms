# 1.4) check if palindrome permutation

def palindrome_permutation(str=''):
    if len(str) < 2:
        return False

    frequencies = {}
    not_even_count = 0

    for char in str.lower():
        if char == ' ':
            continue
        frequencies[char] = 1 + frequencies.get(char, 0)


    for number in frequencies.values():
        if number % 2 != 0:
            not_even_count += 1
            if not_even_count > 1:
                return False
    return True

print(palindrome_permutation('raaaa'))