# 1.5) check if two words are one or less edits away.

def check_edits(str1='', str2=''):
    if str1 == str2:
        return True

    str1_len = len(str1)
    str2_len = len(str2)
    diff = abs(str1_len - str2_len)

    if diff > 1:
        return False

    if str1_len > str2_len:
        return insert_edits(str1, str2)
    elif str1_len < str2_len:
        return insert_edits(str2, str1)
    else:
        return replace_edits(str1, str2)


def replace_edits(str1, str2):
    one_edit = False

    for i in range(len(str2)):
        if str1[i] != str2[i]:
            if one_edit:
                return False
            one_edit = True
    return True


def insert_edits(str1, str2):
    one_edit = False
    index1 = 0
    index2 = 0

    for i in range(len(str2)):
        if str1[index1] != str2[index2]:
            if one_edit:
                return False
            one_edit = True

            index1 += 1
        else:
            index1 += 1
            index2 += 1

    return True


print(check_edits('pales', 'bae'))
