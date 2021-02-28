from functools import wraps

def decorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print(f"you are calling {f.__name__}")
        print(f"{f.__doc__}")
        return f(*args, **kwargs)
    return wrapper

@decorator
def add(a,b):
    '''This function takes two numbers and return their ddition'''
    return a+b

print(add(2,3))