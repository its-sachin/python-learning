def fun(l,str):
    for pos,name in enumerate(l):
        if name == str:
            return pos
    return -1

l = ['sachin', 'the', 'great']
  print(fun(l,'great'))
