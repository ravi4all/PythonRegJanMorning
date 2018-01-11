# Fib Series = 0 1 1 2 3 5 8 13 21 34

a = 1
fib = 0

while fib < 100:
    print(fib, end = ' ')
    a,fib = fib, a+fib
