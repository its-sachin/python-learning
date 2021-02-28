def greater(a,b):
    if a > b:
        return a
    else:
        return b
num1 = int(input("Please input number 1: "))
num2 = int(input("Please input number 2: "))
print(f"greater of two is {greater(num1,num2)}")