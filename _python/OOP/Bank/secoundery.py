from typing import Dict, List, Tuple
from decimal import Decimal, getcontext

class InsufficientFundsError(Exception):
    """Raised when withdrawal amount exceeds account balance"""
    pass

class BankAccount:
    def __init__(self, balance: float, int_rate: float = 0.02):
        """Initialize account with precise decimal arithmetic"""
        getcontext().prec = 6
        if not 0 <= int_rate <= 1:
            raise ValueError("Interest rate must be between 0 and 1")
        self.balance = Decimal(str(balance))
        self.int_rate = Decimal(str(int_rate))
        self.transaction_history: List[Tuple[str, Decimal]] = []

    def deposit(self, amount: float) -> 'BankAccount':
        """Deposit money with validation"""
        amount_dec = Decimal(str(amount))
        if amount_dec <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount_dec
        self.transaction_history.append(('deposit', amount_dec))
        return self

    def withdraw(self, amount: float) -> 'BankAccount':
        """Withdraw money with overdraft protection"""
        amount_dec = Decimal(str(amount))
        if amount_dec <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if self.balance < amount_dec:
            raise InsufficientFundsError(
                f"Insufficient funds. Available: {float(self.balance):.2f}, "
                f"Attempted: {float(amount_dec):.2f}"
            )
        self.balance -= amount_dec
        self.transaction_history.append(('withdraw', amount_dec))
        return self

    def yield_interest(self) -> 'BankAccount':
        """Calculate and deposit interest"""
        interest = self.balance * self.int_rate
        if interest > 0:
            return self.deposit(float(interest))
        return self

    def get_transaction_history(self) -> List[Tuple[str, float]]:
        """Return transaction history as float tuples"""
        return [(action, float(amount)) for action, amount in self.transaction_history]

class User:
    def __init__(self, user_name: str, user_email: str):
        """Initialize user with account management"""
        if not isinstance(user_name, str) or not user_name.strip():
            raise ValueError("User name must be a non-empty string")
        if "@" not in user_email or "." not in user_email:
            raise ValueError("Invalid email format")
        self.name = user_name.strip()
        self.email = user_email.lower().strip()
        self.accounts: Dict[str, BankAccount] = {}

    def create_account(
        self, 
        account_type: str, 
        balance: float = 0, 
        int_rate: float = 0.02
    ) -> 'User':
        """Create new account with validation"""
        if not isinstance(account_type, str) or not account_type.strip():
            raise ValueError("Account type must be a non-empty string")
        if account_type.lower() in {k.lower() for k in self.accounts}:
            raise ValueError(f"Account type '{account_type}' already exists")
        
        self.accounts[account_type] = BankAccount(balance, int_rate)
        return self

    def transfer_money(
        self, 
        from_account: str, 
        to_user: 'User', 
        to_account: str, 
        amount: float
    ) -> 'User':
        """Transfer money between accounts with full validation"""
        # Validate accounts exist
        if from_account not in self.accounts:
            raise ValueError(f"Source account '{from_account}' not found")
        if to_account not in to_user.accounts:
            raise ValueError(f"Target account '{to_account}' not found in recipient")
        
        # Perform atomic transfer
        try:
            self.accounts[from_account].withdraw(amount)
            to_user.accounts[to_account].deposit(amount)
        except Exception as e:
            # Rollback in case of partial failure
            if to_user.accounts[to_account].transaction_history \
               and to_user.accounts[to_account].transaction_history[-1][0] == 'deposit' \
               and to_user.accounts[to_account].transaction_history[-1][1] == Decimal(str(amount)):
                to_user.accounts[to_account].withdraw(amount)
            raise ValueError(f"Transfer failed: {str(e)}")
        
        return self

    def get_account_balances(self) -> Dict[str, float]:
        """Return all account balances"""
        return {name: float(acc.balance) for name, acc in self.accounts.items()}
try:
    # Create users
    alice = User("Alice Smith", "alice@example.com")
    bob = User("Bob Johnson", "bob@example.com")

    # Create accounts
    alice.create_account("checking", 1000.50)
    alice.create_account("savings", 5000, 0.05)
    bob.create_account("primary", 2000)

    # Perform transactions
    alice.transfer_money("checking", bob, "primary", 250.75)
    
    # Yield interest
    alice.accounts["savings"].yield_interest()
    
    # Check balances
    print("Alice's balances:", alice.get_account_balances())
    print("Bob's balances:", bob.get_account_balances())

except Exception as e:
    print(f"Error: {str(e)}")