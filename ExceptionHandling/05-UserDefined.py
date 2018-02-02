def login():
    pin = int(input("Enter your PIN : "))

    if pin == 1234:
        menu()


def menu():
    total_bal = 25000
    print("Welcom to HDFC Bank")

    print("""
    1. Withdraw
    2. Deposit
    3. Balance Check
    4. PIN Change
    """)
    userchoice = input("Enter your choice : ")
    try:
        if userchoice == "1":
            amount = int(input("Enter the amount you want to withdraw : "))
            if total_bal < amount:
                # print("Insufficient balance...")
                raise ValueError("Insufficient balance...")
            else:
                total_bal = total_bal - amount
                print(total_bal)
    except ValueError as error:
        print(error)

    print("Transaction Complete...")

login()