class Bank:
    def set_details(self, name, balance = 0):
        self.name = name
        self.balance = balance

    def display(self):
        print('Name:', self.name)
        print('Balance:', self.balance)
    
    def withdraw(self):
        self.balance -= 1000

    def deposit(self):
        self.balance += 5000

test_1 = Bank()
test_2 = Bank()

test_1.set_details('Reddmar', 30000)

test_1.display()

test_1.deposit()
test_1.deposit()
test_1.deposit()
test_1.deposit()

test_1.display()

test_1.withdraw()
test_1.withdraw()
test_1.withdraw()

test_1.display()

test_2.set_details('Fran')

test_2.display()

test_2.deposit()
test_2.withdraw()

test_2.display()