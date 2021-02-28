import numpy as np

def insertion_sort(a):
    # assert : array a is established
    i = 0
    # INV : a[0..i-1] is sorted 0 <= i <= len(a)
    while (i < len(a)):
        x = a[i]
        j = i

        # INV :  all a[j+1...i-1] > x; 0 <= j <= i
        while (j > 0) & (a[j-1] > x):
            a[j] = a[j-1]
            j = j-1

        # assert : all a[0...j-1] < x and all a[j+1...i-1] > x
        a[j] = x
        i = i + 1
    return(a)

    # assert : array a is sorted

n = 10
a = np.random.randint(0,n,n)
print(a)
print(insertion_sort(a))