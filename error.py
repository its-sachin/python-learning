def fun(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print('Please dont divide by 0... We dont do that here.')
    except:
        print('Invalid input')
    
print(fun(2,0))



        
