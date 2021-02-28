import numpy as np

def sequential_search(a,x):
    # assert : array a and element x are established
    i = 0
    found = False
    # INV : (x not found in a[0..i-1], found = False) 0 <= i <= len(a)

    while (i < len(a)) & (not found):
        if a[i] == x:
            found = True
        else:
            i += 1

    # assert (x found in a at i, a[i] = x) or (x not found in a)

    if found:
        return i
    else:
        return -1

n = 10
a = np.random.randint(0,n,n)
print(a)
print(sequential_search(a,7))