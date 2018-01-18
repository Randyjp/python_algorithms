def compress(string):
    counter = 1
    result = []

    for i in range(len(string)):
        if not (i + 1) == len(string) and string[i] == string[i + 1]:
            counter += 1
        else:
            result.append(string[i] + str(counter))
            counter = 1

    final = "".join(result)

    if len(string) > len(final):
        return final
    return string

print(compress('rrrrrrqqqqqqaaaaddddaaaadda'))