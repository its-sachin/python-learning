import numpy as np

def binary_search(a,x):
    # assert : array a and x are established; a is sorted
    left = 0
    right = len(a)-1
    found = False
    # INV : (x not in a[0...left-1] and a[right+1.....len(n)-1]) 0 <= left <= right < len(a)

    while (left <= right) & (not found):
        i = (left+right)//2
        if (a[i] == x):
            found = True
        elif (a[i] > x):
            right = i-1
        else:
            left = i+1
        
    # assert : (found => a[i] = x) or (x not in a[0...len(a)-1])

    if found:
        return i
    else:
        return -1

n = 100
a = np.random.randint(0,n,n)
print(a)
print(binary_search(a,70))