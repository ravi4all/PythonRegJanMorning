def closures(x):

    def inner(y):
        return x + y

    return inner

def closure_2(x):
    return lambda y : x + y

closure1 = closures(12)
print(closure1(10))

closure2 = closure_2(5)
print(closure2(10))
