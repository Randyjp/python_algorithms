# 8.7) write a program that writes the permutations of a word with no duplicates

def permutations(word):
    if len(word) == 1:
        return word

    word_list = list(word)
    result = []

    for i in range(len(word)):
        temp = word_list.pop(i)
        temp_perm = permutations(''.join(word_list))
        result += [temp + x for x in temp_perm]
        word_list.insert(i, temp)

    return result


# test code

worxd = 'two'
final = permutations(worxd)
print(final)
