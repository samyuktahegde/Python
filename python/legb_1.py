def outer():
    x = 'Outer x' 
    def inner():
        global x
        # nonlocal x
        x = 'inner x'
        print(x)
    inner()
    print(x)

outer()

