message = "Welcome User"
print(message.center(50))

while True:
    user_input = input("Enter your message : ")

    if user_input.lower() == 'hi':
        print("Hi")
    elif user_input.lower() == 'good morning':
        print('Good Morning')
    elif user_input == 'bye' or user_input == 'Bye':
        print('Bye')
        break
    else:
        print("I don't understand")
