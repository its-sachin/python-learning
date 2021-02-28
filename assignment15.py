def oven_filter(l):
    odd = []
    even = []
    for i in l:
        if int(i)%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return [odd, even]
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(oven_filter(list))