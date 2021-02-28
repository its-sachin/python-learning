def sublist_counter(l):
    count = 0
    for i in l:
        if type(i) == list:
            count += 1
    return count

lists = [1, 2, 3, [2, 3], [4, 5]]
print(sublist_counter(lists))
