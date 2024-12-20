# Carl Giroulle - bank_account

class Bankaccount:
    def __init__(self, account_id, pin_code, holder_name, balance):
        self.account_id = account_id
        self.pin_code = pin_code
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self,money_add):
        if money_add > 0:
            amount = self.balance + money_add
            self.balance = amount
        elif money_add <= 0:
            print("Can't deposit zero or a negative number!")

    def withdraw(self, money_sub):
        if money_sub > 0:
            if money_sub <= self.balance:
                amount = self.balance - money_sub
                self.balance = amount
        elif money_sub <= 0:
            print ("Can't withdraw a negative number")
