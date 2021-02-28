name = input("Please write your name: ")
i = 0
temp = ""
while i < len(name):
    count = (name[i])
    if count not in temp:
         print(f"{count} = {name.count(count)}")
    temp += count
    i += 1
    