def fibo(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    elif n == 2:
        print(a, b)
    else:
        print(a, b, end = " ")
        for m in range(0, n-2):
            c = a + b
            a = b
            b = c
            print(b, end = " ")
        
num = int(input("Please type number upto which you want fibonacci seriers to be extended: "))
print(fibo(num))