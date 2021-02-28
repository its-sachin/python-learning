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
L = [1.585,1.605,1.621,1.641,1.667,1.687,1.704,1.729,1.749,1.768,1.785,1.8,1.826]
M = [6.907,8.006,8.517,9.392,10.203,10.859,11.373,12.138,12.709,13.203,13.622,13.971,14.498]

# Exp b:
# l = [289,291,292,295,297,299,302,303,305,307,310,312,314,316,317,320,321,324,326,328,331,333,336,338,342,344,347]
# m = [2.81,2.66,2.66,2.52,2.407,2.302,2.2,2.12,2.04,1.966,1.83,1.77,1.66,1.61,1.56,1.469,1.386,1.31,1.204,1.139,.994,.941,.849,.755,.63,.545,.415]
# L= []
# for i in l:
#     L.append(1000/i)
# M= []
# for i in m:
#     M.append(-i)
funC(L,M)
    