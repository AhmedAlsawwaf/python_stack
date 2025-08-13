class User:
    def __init__(self, user_name, user_email):
        self.name = user_name
        self.email = user_email
        self.accounts = {}
    
    def create_account(self, account_type, balance=0, int_rate=0.02):
        self.accounts[account_type] = BankAccount(balance, int_rate)
        return self
    
    def get_account(self, account_type):
        if account_type not in self.accounts:
            print(f"Error: {self.name} has no account named '{account_type}'")
            return self
        return self.accounts.get(account_type)
    
    def transfer_money(self, from_account, to_user, to_account, amount):
        if self.accounts[from_account].balance < amount:
            print("You do not have enough credit")
            return self
        if from_account not in self.accounts:
            print(f"Error: {self.name} has no account named '{from_account}'")
            return self
        
        if to_account not in to_user.accounts:
            print(f"Error: {to_user.name} has no account named '{to_account}'")
            return self
        
        self.accounts[from_account].withdraw(amount,from_account)
        to_user.accounts[to_account].deposit(amount,to_account)
        
        print(f"Transfer complete: {amount} from {self.name}'s {from_account} to {to_user.name}'s {to_account}")
        return self

class BankAccount:
    def __init__(self, balance, int_rate):
        self.balance = balance
        self.int_rate = int_rate

    def deposit(self, amount, account_type=None):
        self.balance += amount
        if account_type:
            print(f"Dear customer, please note that {amount} was deposited to your {account_type} account. Your balance is now {self.balance}")
        return self

    def withdraw(self, amount, account_type=None):
        if self.balance < amount:
            print("You do not have enough credit")
            return self
        self.balance -= amount
        if account_type:
            print(f"Dear customer, please note that {amount} was withdrawn from your {account_type} account. Your balance is now {self.balance}")
        return self
    
    def display_account_info(self):
        print(f"Your balance is {self.balance}")
        return self
    
    def yield_interest(self, account_type):
        added_amount = self.int_rate * self.balance
        print(f"Your interest: {added_amount} added to your {account_type} account")
        self.deposit(added_amount, account_type)
        return self

# create users
ahmed = User("ahmed", "ahmed@gmail.com")
ali = User("ali", "ali@g.co")
ahmed.create_account("current", 1000).create_account("savings", 5000, 0.05)
ali.create_account("current", 1000).create_account("savings", 3000, 0.05)

# Testing
ahmed.get_account('savings').display_account_info()
ali.get_account('current').display_account_info()
ahmed.transfer_money("savings", ali, "current", 30000)
ahmed.transfer_money("savings", ali, "current", 300)
ahmed.get_account('savings').display_account_info()
ali.get_account('current').display_account_info()
ahmed.get_account("current").withdraw(500000,"current") 
ahmed.get_account("current").withdraw(500,"current") 