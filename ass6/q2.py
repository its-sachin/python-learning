def fun(l,a):
    i = 0
    k = l.copy()
    while i < len(k):
        if k[i] > a:
            l.remove(k[i])
            l.append(k[i])
        i += 1
    return l

l = [28,26,25,11,16,12,24,29,6,10]
a = 17

print(fun(l,a))