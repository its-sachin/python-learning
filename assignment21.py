def integer(l):
    r = [str(i) for i in l if (type(i) == int or type(i) == float) ]
    return r
list1 = [1, 1.1, 'sachin', 23, [1, 2, 3] ]
print(integer(list1))