# --- A program written in fulfillment of the Zuri tasks
#  --- 24/4/2021

import random
from datetime import *

bank_time = datetime.now()
bank_time_1 = bank_time.strftime("%Y-%m-%d %H:%M:%S")

database = {
    2101668622: ["sten", "techy", "stentechy@zuri.com", "password", 4000]
}

balance = 0


def initialise():
    if bank_time.strftime("%p") == "AM":
        print("Good Morning")
        print(bank_time)

    else:
        print("Good Evening")
        print(bank_time)

    print("Welcome to Bank of STEN")

    have_account = int(input("Do you have an account with us:\n 1. (YES)\n 2. (NO)\n"))

    if have_account == 1:
        login()
    elif have_account == 2:
        register()
    else:
        print("You have selected an invalid option")
        print("=" * 35)
        initialise()


def login():
    print("=" * 9 + " Login " + "=" * 9)
    user_account_number = int(input("Enter your Account number: \n"))

    is_account_number_valid = account_number_validation(user_account_number)

    # To check the code
    # print(is_account_number_valid)

    if is_account_number_valid:
        user_password = input("Enter your Password: \n")

        for account_number, user_details in database.items():

            if account_number == user_account_number:

                if user_details[3] == user_password:
                    bank_operation(account_number, user_details)
                else:
                    print("invalid password")
            elif account_number != user_account_number:
                print("Invalid Account Number")

        print("Please try again")
        login()


def register():
    print("-" * 9 + " Register Below" + "-" * 9)

    email = input("Please enter your email: \n")

    first_name = input("Please enter your First Name: \n")

    last_name = input("Please enter your Last Name: \n")

    password = input("Create a Password: \n")

    is_password_valid = registration_input_validation(password)

    if is_password_valid:
        account_number = int(account_number_generation())

        database[account_number] = [first_name, last_name, email, password, balance]

        # to check the database
        print(database[account_number])

        print("Congratulations, your account has been created")
        print("=" * 15 + " " * 5 + "=" * 15)
        print(f"Your account number is: {account_number}")
        print("Make sure to keep it safe")
        print("=" * 15 + " " * 5 + "=" * 15)

        login()


def account_number_validation(account_number):
    if account_number:

        if len(str(account_number)) == 10:

            try:
                int(account_number)
                return True
            except ValueError:
                print("Invalid account number, account number should contain only real numbers")
                login()
                return False
            except TypeError:
                print("Invalid account type")
                login()
                return False

        else:
            print("Account number should not be less or more than ten digits")
            login()
            return False

    else:
        print("Account number is a required field")
        login()


def registration_input_validation(password):
    if password:

        if len(str(password)) >= 8:

            try:
                str(password)
                return True
            except ValueError:
                register()
                return False

        else:
            print("Password should not be less than eight(8)")
            register()
            return False

    else:
        print("Password is required")


def bank_operation(account_number, user_details):
    print(f"Welcome {user_details[0]} {user_details[1]}")

    selected_option = int(input("What would you like to do? \n (1). Deposit \t (2). Withdraw \n "
                                "(3). View Balance \t (4). Contact customer care \n (5). Cancel \t (6). Exit \n"))

    if selected_option == 1:
        deposit(account_number, user_details)
    elif selected_option == 2:
        withdrawal(account_number, user_details)
    elif selected_option == 3:
        view_balance(account_number, user_details)
    elif selected_option == 4:
        customer_care(account_number, user_details)
    elif selected_option == 5:
        login()
    elif selected_option == 6:
        exit()

    else:
        print("Invalid option selected, please tyr again")

        print("=" * 20, "  " * 5, "=" * 20)

        bank_operation(account_number, user_details)


def withdrawal(account_number, user_details):
    user_withdrawal = int(input("How much do you want to withdraw: \n"))
    current_balance = ((database[account_number])[4])

    if current_balance < user_withdrawal:
        print("Insufficient balance")

        print("=" * 20, "  " * 5, "=" * 20)

        bank_operation(account_number, user_details)

    elif current_balance >= user_withdrawal:
        current_balance = current_balance - user_withdrawal
        print(f"You have successfully withdrawn {user_withdrawal} NGN")
        print("Please take your cash")
        print(f"Your current balance is {current_balance} NGN")

        ((database[account_number])[4]) = current_balance

        print("=" * 20, "  " * 5, "=" * 20)

        bank_operation(account_number, user_details)


def deposit(account_number, user_details):
    user_deposit = float(input("Input amount to deposit: \n"))
    new_balance = ((database[account_number])[4])
    new_balance = user_deposit + new_balance
    ((database[account_number])[4]) = new_balance

    print(f"You have successfully deposited {user_deposit} NGN")
    print(f"Your current balance is {new_balance} NGN")

    print("=" * 20, "  " * 5, "=" * 20)

    bank_operation(account_number, user_details)


def view_balance(account_number, user_details):
    current_balance = ((database[account_number])[4])
    print("Your account balance is: ", current_balance)

    print("=" * 20, "  " * 5, "=" * 20)

    bank_operation(account_number, user_details)


def customer_care(account_number, user_details):
    print("You can the customer care via \n (1). Whatsapp: 09068565663 \n (2). Twitter: StenTechy \n (3). Instagram: "
          "Sten Techy")

    print("=" * 20, "  " * 5, "=" * 20)

    bank_operation(account_number, user_details)


def logout():
    login()


def account_number_generation():
    return random.randrange(1111111111, 9999999999)


initialise()

# --- I faced an issue implementing "ValueError", the program keeps bringing up value errors even though i exempted it.
# --- ValueError: invalid literal for int() with base 10: 'rrrr5555'
