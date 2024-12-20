from bank_account_maarten import BankAccount

accounts = []
accounts.append(BankAccount(
    "BE7800",
    1234,
    "Maarten Weckhuysen",
    "150000"
))

accounts.append(BankAccount(
    "BE7801",
    1234,
    "Hagrid",
    "450222"
))

accounts.append(BankAccount(
    "BE7802",
    1234,
    "Joske Vermeulen",
    "988555"
))



wrong_pin_count = 0


while True:
    logout = False
    login_account_id = input("What is your bank account?: ")
    if login_account_id != "":
        account = BankAccount.find_account(accounts, login_account_id)
        if (login_account_id == account.account_id):
            login_account_pincode = int(input("What is your pincode?: "))
            if login_account_pincode == account.pin_code:
                print(f"\nWelcome, {account.holder_name} to our ATM application")
                while logout == False:
                    selection = int(
                        input(f"""
                            **************************************
                            **************************************
                            **          ATM Application         **
                            **************************************
                            **************************************
                            **************************************
                            **     Your balance: {account.balance}       **
                            **************************************
                            * 1) Withdraw money                  *
                            * 2) Deposit money                   *
                            * 3) Exit                            *
                            **************************************
                            Select an option (1-3): """))

                    if selection == 1:
                        amount = float(input(f"How many do you want to deposit (EUR): "))
                        account.withdraw(amount)

                    elif selection == 2:
                        amount = float(input(f"How many do you want to withdraw (EUR): "))
                        account.deposit(amount)

                    elif selection == 3:
                        logout = True
                        print(f"""
                        *****************************************
                        **          Shutting down ...          **
                        **   Thank you for using ATM app       **
                        ** Have a nice day, {account.holder_name} **
                        *****************************************
                        """)
                        #break

            elif wrong_pin_count < 2:
                print("!!!! Wrong pincode !!!!")
                print(f"{2 - wrong_pin_count} attempts left")
                wrong_pin_count += 1

            elif wrong_pin_count == 2:
                print("Too many login attempts, please contact our helpdesk: 0496/086393")
                logout = True
                #break

    elif login_account_id == "":
        break