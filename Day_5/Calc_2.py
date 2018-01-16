# DRY - Donot Repeat Yourself

def add(x,y):
    result = x + y
    print(result)

def sub(x,y):
    result = x - y
    print(result)

def div(x,y):
    result = x / y
    print(result)

def mul(x,y):
    result = x * y
    print(result)

def err_handler(*args):
    print("You have pressed something wrong...")

def quitCalc(*args):
    quit()

while True:

    print("""
    1. Add
    2. Sub
    3. Div
    4. Mul
    5. Quit
    """)

    user_input = input("Enter your choice : ")

    num_1 = int(input("Enter first number : "))
    num_2 = int(input("Enter second number : "))

    todo = {
        "1" : add,
        "2" : sub,
        "3" : div,
        "4" : mul,
        "5" : quitCalc
        }

    ##todo[user_input](num_1,num_2)

    todo.get(user_input, err_handler)(num_1,num_2)
