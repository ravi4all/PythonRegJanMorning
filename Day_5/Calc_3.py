# DRY - Donot Repeat Yourself

def calculator(x,y,opr):
    expression = x + opr + y
    result = eval(expression)
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

    num_1 = input("Enter first number : ")
    num_2 = input("Enter second number : ")

    todo = {
        "1" : "+",
        "2" : "-",
        "3" : "/",
        "4" : "*",
        "5" : quitCalc
        }

    ##todo[user_input](num_1,num_2)

    #todo.get(user_input, err_handler)(num_1,num_2,user_input)

    opr = todo.get(user_input)

    calculator(num_1,num_2,opr)
