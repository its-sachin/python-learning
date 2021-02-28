def fun(l):
    rev = []
    for i in l:
        rev.append(i[::-1])
    return rev
list = ['sachin', 'sain', 'great']
print(fun(list))