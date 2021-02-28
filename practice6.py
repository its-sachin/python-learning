def greater(a,b,c):
    if a > b and a > c:
        return a
    elif b > c and b > a:
        return b
    elif c > a and c > b:
        return c

num1 = int(input("Please write number 1: "))
num2 = int(input("Please write number 2: "))
num3 = int(input("Please write number 3: "))

print(f"Greatest of all three is {greater(num1,num2,num3)}")