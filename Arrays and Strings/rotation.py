# 1.9) check if string is rotation

def is_rotation(s1, s2):
    new_string = s2 + s2
    return s1 in new_string

print(is_rotation('marca', 'rcama'))