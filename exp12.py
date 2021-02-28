deg = int(input("Please write degree measure: "))
mini = int(input("Please write minute measure: "))
sec = int(input("Please write second measure: "))

def fun(a,b,c):
    return a + b/60 + c/3600      

print(fun(deg,mini,sec))
