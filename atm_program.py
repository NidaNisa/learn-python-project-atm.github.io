from customer import Customer
from atm_card import ATMCard

atm_card = ATMCard()
print()
print("Welcome to {}!".format(atm_card.name))
print()
running = True
while running:
    print()
    print("""Choose an option:

    1. Open new bank account
    2. Open existing bank account
    3. Exit
    """)

    choice = int(input("1, 2 or 3: "))

    if choice == 1:
        print()
        print("To create an account, please fill in the information below.")
        print()
        customer = Customer(input("ID: "), int(input("Deposit amount: ")))
        atm_card.update_db(customer)
        print()
        print("Account created successfully! Your pin is: ", customer.account['custPin'])
    elif choice == 2:
        print()
        print("To access your account, please enter your credentials below.")
        print()
        id = input("ID: ")
        custPin = int(input("PIN: "))
        current_client = atm_card.authentication(id, custPin)
        if current_client:
            print()
            print("Welcome {}!".format(current_client.account['id']))
            acc_open = True
            while acc_open:
                print()
                print("""WELCOME TO PROGATE BANK
                
    Choose an option:
    1. Withdraw
    2. Deposit
    3. Balance
    4. Transfer
    5. Exit
                    """)
                acc_choice = int(input("1, 2, 3, 4 or 5: "))
                if acc_choice == 1:
                    print()
                    current_client.withdraw(int(input("Withdraw amount: ")))
                elif acc_choice == 2:
                    print()
                    current_client.deposit(int(input("Deposit amount: ")))
                elif acc_choice == 3:
                    print()
                    current_client.balance()
                elif acc_choice == 4:
                    print("To Transfer Money, Please Enter Destination Account Number")
                    id = input("ID to transfer: ")
                    if current_client:
                        print("Account number found, please enter the nominal to be transferred")
                        current_client.transfer(int(input("Transfer amount: ")))
                        print()
                        current_client.balance()
                    else:
                        print("Destination Account Number Not found or not registered")
                        print()
                        current_client.balance()
                elif acc_choice == 5:
                    print()
                    print("Thank you for visiting!")
                    current_client = ''
                    acc_open = False
        else:
            print()
            print("Authentication failed!")
            print("Reason: account not found.")
            continue
    elif choice == 3:
        print()
        print("Goodbye!")
        running = False