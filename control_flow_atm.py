# Initial balance in the account
balance = 10000

# PIN for account access
pin = 1234

# Get user input for PIN
user_input = input("Please enter your pin: ")

# Available choices for the user
withdraw_choice = "withdraw"
deposit_choice = "deposit"
exit_choice = "exit"

# Check if the entered PIN matches the account's PIN
if int(user_input) == pin:
    # Display current balance
    print("Your current balance is:", balance)

    # Prompt user to select an action
    print("Please choose one of the following options: withdraw, deposit, or exit")
    atm_choice = input().lower()

    # Perform the selected action
    if atm_choice == withdraw_choice:
        # Withdrawal process
        withdraw_amount = int(input("How much would you like to withdraw: "))
        if withdraw_amount <= balance:
            balance -= withdraw_amount
            print("Your balance is now:", balance)
        else:
            print("You cannot withdraw more than what you have in your account.")
    elif atm_choice == deposit_choice:
        # Deposit process
        deposit_amount = int(input("How much would you like to deposit: "))
        balance += deposit_amount
        print("Your total balance is now:", balance)
    elif atm_choice == exit_choice:
        # Exit the ATM
        print("Thank you for using the ATM, hope to see you again!")
    else:
        # Invalid choice
        print("Please enter a valid option.")
else:
    # Incorrect PIN
    print("Incorrect pin, please try again.")
