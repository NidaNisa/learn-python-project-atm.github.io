from random import randint


class Customer:

    # {id: "xxxxx:, custPin: xxxxxx, custBalance: xxxx}
    account = {}

    def __init__(self, id, deposit):
        self.account['id'] = id
        self.account['custPin'] = randint(10000, 99999)
        self.account['custBalance'] = deposit

    def withdraw(self, amount):
        if self.account['custBalance'] >= amount:
            self.account['custBalance'] -= amount
            print()
            print("The sum of {} has been withdrawn from your account balance.".format(amount))
            self.balance()
        else:
            print()
            print("Not enough funds!")
            self.balance()

    def deposit(self, amount):
        self.account['custBalance'] += amount
        print()
        print("The sum of {} has been added to your account balance.".format(amount))
        self.balance()

    def transfer(self, amount):
        if self.account['custBalance'] >= amount:
            self.account['custBalance'] -= amount
            print()
            print("The sum of {} has been withdrawn from your account balance.".format(amount))
            self.balance()
        else:
            print()
            print("Not enough funds!")
            self.balance()
    def balance(self):
        print()
        print("Your current account balance is: {} ".format(self.account['custBalance']))