def common(l, f):
    ret = []
    for i in l:
        if i in f:
            ret.append(i)
    return(ret)

list1 = [1,5,6,8]
list2 = [2,5,7,8]
print(common(list1, list2))