def funC(l,m):
    n = len(l)
    a = 0
    for i in l:
        a += i
    b = 0
    for i in l:
        b += i*i
    c = 0
    for i in m:
        c += i
    d = 0
    for i in range (len(l)):
        d += l[i]*m[i]
    print(f"value of submission x is : {a}")
    print(f"Value of submission y is : {c}")
    print(f"Value of submission xy is : {d}")
    print(f"Value of submission x^2 is : {b}")
    print(f"No. of entries are : {n}")
    print(f"Square fitting slope is : {(a*c - d*n)/(a*a - n*b)}")

# Exp a:
# L = [1.585,1.605,1.621,1.641,1.667,1.687,1.704,1.729,1.749,1.768,1.785,1.8,1.826]
# M = [6.907,8.006,8.517,9.392,10.203,10.859,11.373,12.138,12.709,13.203,13.622,13.971,14.498]

# Exp b:
l = [6.105,6.013,5.279,4.137,4.038,3.353,3.003,2.983]
m = [1.683,1.6802,1.669,1.659,1.657,1.649,1.647,1.646]
# L= []
# for i in l:
#     L.append(1000/i)
# M= []
# for i in m:
#     M.append(-i)
# K = []
# for i in l:
#     K.append(i - 273.15)

funC(l,m)
# print(K)