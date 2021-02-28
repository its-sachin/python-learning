def rev(l):
    reverse = []
    for i in l:
        reverse.insert(0, i)
    return reverse
lists = list(range(1,11))
print(rev(lists))
