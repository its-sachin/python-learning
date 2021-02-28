def append(a,b):
    for i in b:
        a.append(i)
    return a 

a = [1,2,3,4,5]
b = [6,7,8,9,0]
print(append(a,b))
