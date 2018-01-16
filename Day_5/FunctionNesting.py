def outer():
    print("this is outer function")
    def inner():
        print("this is inner function")
        def innermost():
            print("this is innermost function")

        return innermost
    
    return inner

inner = outer()
innermost = inner()
innermost()
