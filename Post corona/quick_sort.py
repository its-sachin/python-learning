import numpy as np

def partition_sir(a,x,left,right):
    # assert : array a[left..right] is established; x is established
    i = left
    j = right
    # INV : all a[0..i-1] <= x and all a[j+1...right] > x; left <= i <= right+1; left -1 <= j <= right; i <= j
    while (i<=j):
        if (a[i] <= x):
            i = i +1
        else:
            a[i],a[j] = a[j],a[i]
            j = j-1
    p = j
    # assert: p such that all a[left....p] <= x and all a[p+1....right] > x
    return p




# def quick_sort(a):
#     # assert: array a is established
#     x = a[0]
#     p = partition(a,left,)

#     # asset : p such that all a[0....p-1] < x and all a[p+1.....len(a)-1] > x

#     # assert : array a is sorted