def CeilIndex(A,l,r,key):
    while r-l > 1:
        m = l + ((r-l)//2)
        if A[m] >= key:
            r = m
        else:
            l= m
        print(l,r)
    return r

def fun(A,size):
    tailTable = [0 for i in range(size +1)]
    len = 0

    tailTable[0] = A[0]
    len = 1

    for i in range(1,size):
        if A[i] < tailTable[0]:
            tailTable[0] = A[i]

        elif A[i] > tailTable[len-1]:
            tailTable[len] = A[i]
            len += 1
        else:
            tailTable[CeilIndex(tailTable,-1,len-1,A[i])] = A[i]
        print(tailTable)
    return len


l = [1,2,9,4,7,3,11,8,14,6]
# l =[6,7,3,4,5]
# l = [3,4,-1,5,8,2,3,12,7,9,10]
print(fun(l,10))
# print(CeilIndex([3,7,0,0,0,0],-1,1,4))
