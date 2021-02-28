def fun(l):
    i = 0
    k = []
    while i < len(l):
        j = 0
        k.append(1)
        while j < i:
            if l[j] < l[i]:
                k[i] = max(k[j] + 1,k[i]) 
            j += 1
        i +=1
    return max(k),k

# l = [1,2,9,4,7,3,11,8,14,6]
# l = [3,4,-1,5,8,2,3,12,7,9,10]
l =[6,7,3,4,5]
print(fun(l))
            