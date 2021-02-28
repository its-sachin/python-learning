def fun(n,x):
    return 333*sin(x*3.14/180)/n

order = int(input("Please write the order: "))
theta = int(input("Please write angle in degree: "))

print(fun(order,theta))