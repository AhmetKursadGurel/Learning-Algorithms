def test_func(a,b,c):
    if c==0:
        print('Code produced ZeroDivisionError')
        return None
        

    try:
        return (a+b)/c

    
    except TypeError :

        print("Code produced TypeError")
        return None

