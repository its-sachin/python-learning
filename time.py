from functools import wraps
import time

def time_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        value = f(*args, **kwargs)
        t2 = time.time()
        print(f"Time taken to run this code is {t2-t1} seconds")
        return value
    return wrapper

@time_decorator
def fun(l):
    i = 0
    k = []
    out = [] 
    while i < len(l):
        j = 0
        k.append(1)
        while j < i:
            if l[j] < l[i]:
                k[i] = max(k[j] + 1,k[i]) 
            j += 1
        i +=1
    return max(k)

import random
l = []
for i in range(1,10000): l.append(random.randint(1,1000000))
print(fun(l))