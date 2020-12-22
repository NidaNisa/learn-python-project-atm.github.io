class ATMCard:

    name = 'Progate Bank'
    customers = []

    def update_db(self, customer):
        self.customers.append(customer)

    def authentication(self, id, custPin):
        for i in range(len(self.customers)):
            if id in self.customers[i].account.values() and custPin in self.customers[i].account.values():
                print()
                print("Authentication successful!")
                return self.customers[i]