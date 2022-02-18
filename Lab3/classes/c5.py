class Account:

    def __init__(self, owner: str):
        self.owner = owner
        self.balance = 0

    def deposit(self, x: int):
        self.balance += x
        print(f'Your balance: {self.balance}\n')

    def withdraw(self, x: int):
        if self.balance - x < 0:
            print('Insufficient funds\n')
        else:
            self.balance -= x
            print('Withdrawal completed successfully')
            print(f'Your remaining balance: {self.balance}\n')

    def show(self):
        print(f'Owner: {self.owner}')
        print(f'Your current balance: {self.balance}\n')

acc1 = Account('Aidana')
acc1.deposit(100)
acc1.show()
acc1.withdraw(150)
acc1.deposit(100)
acc1.withdraw(150)