def mod_max(a1,a2):
    i = 0
    val = 0
    while i < len(a1):
        j = i
        while j < len(a1):
            inter = abs(int(a1[i]) - int(a1[j])) + abs(int(a2[i]) - int(a2[j])) +  abs(i-j)
            if inter > val :
                val = inter
            j += 1
        i += 1
    return val

a1 = [1,2,3,4] 
a2 = [-1,4,5,6]

print(mod_max(a1,a2))