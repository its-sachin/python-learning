def swap(a,i,j):
    try:
        intermediate = a[i]
        a[i] = a[j]
        a[j] = intermediate
    except:
        pass
    return a

def selcetion_sort(a):
    i = 0
    while i < len(a):
        min = a[i]
        index = i
        j = i
        while j < len(a):
            if a[j] < min:
                min = a[j]
                index = j
            j += 1
        a = swap(a,i,index)
        i += 1

    return a
        
a = [3,2,1,4,5,0,-1,99,45,90,12]
print(selcetion_sort(a))     