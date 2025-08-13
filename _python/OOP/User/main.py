class User:
    def __init__(self,user_name,user_email, balance = 0):
        self.name = user_name
        self.email = user_email
        self.balance = balance
        self.last_transaction = ""
    def make_deposit(self,amount):
        self.balance += amount
        self.last_transaction = f"+{amount}"
        print(f"{amount} deposit to your acount, your balance is {self.balance}")
        return self
    
    def make_withdraw(self,amount):
        self.balance -= amount
        self.last_transaction = f"-{amount}"
        print(f"{amount} withdraw from your acount, your balance is {self.balance}")
        return self
    
    def user_balance(self):
        print (f"{self.name} balance is = {self.balance} ")
        return self
    
    def transfer_money(self,user_to,amount):
        self.make_withdraw(amount)
        user_to.make_deposit(amount)
        print(f"Hi {self.name} your transaction is done, your balance is {self.balance}")
        return self
# object = instance from the class or copy from the class
ahmed = User("Ahmed","ahmed.2001@gmail.com",100)
ali = User("Ali","ali@gmail.com")
shatha = User("Shatha","shatha@gmail.com",50)

print(ahmed.name)
print(ahmed.email)
print(ahmed.balance)

ahmed.make_deposit(100).make_withdraw(45).user_balance().transfer_money(shatha,100)

shatha.transfer_money(ali,50)
ali.user_balance()