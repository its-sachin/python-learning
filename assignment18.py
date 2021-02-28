def cube(n):
    d = {}
    for i in range(1, n+1):
        d[i] = i**3
    return d 
num = int(input("Please write the number : "))
print(cube(num))       