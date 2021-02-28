def fun(l,k):
    n = []
    for i in l:
        if len(n) < k:
            n.append(i)
        else:
            n.append(i)
            n.remove(max(n))
    return max(n)

l = [1,2,9,4,7,3,11,8,14,6]
print(fun(l,2))

    