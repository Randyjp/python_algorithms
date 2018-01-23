def sub_sets(arr, comb):
    if len(arr) <= 0:
        return
    val = arr.pop()
    new_combs = [[val]]

    for subset in comb:
        # subset.append(val)
        new_combs.append(subset + [val])

    comb += new_combs
    sub_sets(arr, comb)

combi = []
s = [2, 3, 9, 12]
sub_sets(s, combi)
print(combi)

# cosa = []
# cosa.append(1)
# print(cosa)