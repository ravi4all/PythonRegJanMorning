def add(x,y):
    result = x + y
    print(result)

def sub(x,y):
    result = x - y
    print(result)

def div():
    pass

def mul():
    pass


print("""
1. Add
2. Sub
3. Div
4. Mul
""")

user_input = input("Enter your choice : ")

num_1 = int(input("Enter first number : "))
num_2 = int(input("Enter second number : "))

if user_input == "1":
    result = num_1 + num_2
    print("Addition is",result)
elif user_input == "2":
    sub(num_1, num_2)
elif user_input == "3":
    div(num_1,num_2)
elif user_input == "4":
    mul(num_1,num_2)
else:
    print("Wrong choice...")
