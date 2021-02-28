def tnd(l):
    import random
    a = random.randint(0,(len(l)-1))
    b = random.randint(0,(len(l)-1))
    if not a == b:
        print(f"{l[a]} owes {l[b]}")
    else:
        tnd(l) 

l = [44,34,323,445,577]
tnd(l)