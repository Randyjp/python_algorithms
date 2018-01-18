# 1.3) replace all spaces with %20

def urlify(url='', length = 0):
    # temp_url = url.strip()
    # return temp_url.replace(' ', '%20')

    temp_url = url.strip()
    result = ''

    for char in temp_url:
        if char == ' ':
            char = '%20'
        result += char
    return result




new = urlify('MR John Smith    ', 13)
print(new)