name = input("Please write your name : ")
car = ""
for i in range(len(name)):
    if name[i] not in car:
        print(f"{name[i]} = {name.count(name[i])}")
    car += name[i]