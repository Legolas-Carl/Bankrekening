class BankAccount:
    def __init__(self, account_id, pin_code, holder_name, balance):
        self.account_id = account_id
        self.pin_code = pin_code
        self.holder_name = holder_name
        self.balance = float(balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return self.balance
        else:
            raise ValueError("The deposit amount has to be positive.")

    def withdraw(self, amount):
        if self.balance > amount and amount > 0:
            self.balance -= amount
            return self.balance
        else:
            raise ValueError("The withdraw amount has to be positive.")

    def find_account(accounts, login_account_id):
        for account in accounts:
            if account.account_id == login_account_id:
                return account
        return None