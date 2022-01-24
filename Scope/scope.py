# nonlocal used within function


res = 'abc'


def test1():
    # res.append(3)
    global res
    res += '33'

    print(res)
    
    


test1()


def outer():

    res = '123'

    def inner():
        nonlocal res

        res += '4'

        print(res)

    inner()


outer()
