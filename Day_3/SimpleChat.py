import random

hello_intent = ['hello','hi','hey']
bye_intent = ['bye','see you','bie']

message = "Welcome User"
print(message.center(50))

while True:
    user_input = input("Enter your message : ")

    if user_input.lower() in hello_intent:
        print(random.choice(hello_intent))
        #print('how can I help you ?')
    elif user_input.lower() in bye_intent:
        #print("Bye! See you later")
        print(random.choice(bye_intent))
    else:
        print("I don't understand")
