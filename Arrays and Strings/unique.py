# 1.1) String has only unique characters?

str = 'this is string example....wow!!!'
chars = list(str.lower())
freq = {}

if len(str) > 128:  # assuming unicode string
    print('No')

else:
    for char in chars:
        freq[char] = 1 + freq.get(char, 0)

    if max(freq.values()) > 1:
        print("No")
    else:
        print("Yes")
