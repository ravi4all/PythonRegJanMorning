def calc():
    try:
        a = int(input("Enter first number : "))
        b = int(input("Enter second number : "))
        add = a + b
        sub = a - b
        div = a / b
        mul = a * b

        print("Results are", add, sub, div, mul)

    except BaseException as execption:
        # print("You have entered something wrong...Try Again")
        print(execption)
        calc()

calc()