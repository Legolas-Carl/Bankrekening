# Carl Giroulle - atm_app
from bank_account import *

account_id = 10010
pin_code = 5678
holder_name = "Jan Janssens"
balance = 2748.19

ba = Bankaccount(account_id, pin_code, holder_name, balance)
print (ba.account_id)
print (ba.pin_code)
print (ba.holder_name)
print (ba.balance)

Bankaccount.deposit(ba,42)
#print (ba.balance)

Bankaccount.withdraw(ba,20)
#print (ba.balance)



keuze=0
while keuze != 3:
    print(
        f"******************************\n"
        f"******************************\n"
        f"***         ATM App        ***\n"
        f"******************************\n"
        f"******************************\n"
        f"******************************\n"
        f"*** Your balance: €{ba.balance} ***\n"
        f"******************************\n"
        f"******************************\n"
        f"*** 1) Withdraw money ********\n"
        f"*** 2) Deposit money  ********\n"
        f"*** 3) Exit           ********\n"
        f"******************************\n"
        f"*** Select an option (1-3)****\n"
    )
    keuze = int(input(" "))
    if keuze == 1:
        bedrag = int(input("\nHow much do you want to withdraw? "))
        Bankaccount.withdraw(ba, bedrag)
    elif keuze == 2:
        bedrag = int(input("\nHow much do you want to deposit? "))
        Bankaccount.deposit(ba, bedrag)
