num = input("Please write some natural number : ")
total = 0
for i in range(len(num)):
    total += int(num[i])
print(f"Sum of digits in your number is {total}")