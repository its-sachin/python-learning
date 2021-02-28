def func(l, **kwargs):
    if kwargs.get('reversed_str') == True:
        return [i[::-1].title() for i in l ]
    else:
        return [i.title() for i in l]

names = ['sachin', 'sain']
print(func(names))
print(func(names, reversed_str = True))