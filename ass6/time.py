import time

def largest_subseq(l):
    out = [[l[0]]]
    i = 1
    while i < len(l): 
        j = len(out)-1
        while j >= 0:
            # print(out,j)

            if l[i] > out[j][-1]:
                out[j].append(l[i])
                if j < len(out) - 1:
                    if len(out[j+1]) == len(out[j]):
                        out.pop(j+1)
                j = -1

            elif max(l[i:len(l)]) > out[j][-1]:
                if len(out[j]) == 1 or l[i] > out[j][-2]:
                    out[j][-1] = l[i]
                j = -1

            elif j == 0:
                if len(out[0]) == 1:
                    out[0] = [l[i]]
                else:
                    out = [[l[i]]] + out
                j = -1

            else:
                j -= 1
                
        i += 1
    return out[-1],len(out[-1])



def CeilIndex(A,l,r,key):
    while r-l > 1:
        m = l + ((r-l)//2)
        if A[m] >= key:
            r = m
        else:
            l= m
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
    return len    


l = [3,4,-1,5,8,2,3,12,7,9,10,4,5,9,23,11,7,0,-7,24,56,43]

t1 = time.time()
print(largest_subseq(l))
t2 = time.time()

print(fun(l,11))
t3 = time.time()

print(t2-t1)
print(t3-t2)