num = int(input("Please type any number : "))
total = 0
i = 0 
while i < len(str(num)):
    total = total + int(str(num)[i])
    i = i + 1
print(total)
