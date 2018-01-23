# 8.8) write a program that writes the permutations of a word with  duplicates


def permutations(word):
    if len(word) == 1:
        return word

    word_list = list(word)
    result = []
    done = []

    for i in range(len(word)):
        temp = word_list.pop(i)
        if temp in done:
            word_list.insert(i, temp)
            continue

        temp_perm = permutations(''.join(word_list))
        result += [temp + x for x in temp_perm]
        word_list.insert(i, temp)
        done.append(temp)

    return result


# test code

worxd = 'aaaaaaaaaaaa'
final = permutations(worxd)
print(final)