def power(n, *args):
    if args:
        return [i**n for i in args]
    else:
        return "Man...you did not write any tuple or list"  

nums = [2, 6, 7]
print(power(3,*nums))

