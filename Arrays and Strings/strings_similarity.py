import string
import math

trans_table = bytes.maketrans((string.punctuation + string.ascii_uppercase).encode(),
                              (' ' * len(string.punctuation) + string.ascii_lowercase).encode())


def get_file(path):
    try:
        text_file = open(path, 'rb').read()
        return text_file
    except FileNotFoundError:
        FileNotFoundError('File doesn\'t exist')


def get_corpus(file):
    translated = bytes.translate(file, trans_table)
    return translated.decode().split()


def compute_words_frequency(words):
    freq = {}

    for word in words:
        if freq.get(word, 0) > 0:
            freq[word] = freq[word] + 1
        else:
            freq[word] = 1

    return freq


def inner_product(D1, D2):
    sum_prod = 0

    for key in D1.keys():
        if D2.get(key, None):
            sum_prod += D1[key] * D2[key]
    return sum_prod


def vector_angle(D1, D2):
    numerator = inner_product(D1, D2)
    denominator = math.sqrt(inner_product(D1, D1) * inner_product(D2, D2))
    return math.acos(numerator / denominator)


def similarity():
    f1 = get_file('./data/t8.shakespeare.txt')
    f2 = get_file('./data/t5.churchill.txt')

    list1 = get_corpus(f1)
    list2 = get_corpus(f2)

    freq1 = compute_words_frequency(list1)
    freq2 = compute_words_frequency(list2)

    angle = vector_angle(freq1, freq2)

    print(angle)


similarity()