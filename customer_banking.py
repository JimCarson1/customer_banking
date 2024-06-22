# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
import savings_account
import cd_account
        
# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    while True:
        savings_balance = input("Enter savings balance: ")
        if is_float(savings_balance):
            savings_balance = float(savings_balance)
            break
        else:
            print("Savings Balance must be a number.")

    while True:
        savings_interest = input("Enter interest rate: ")
        if is_float(savings_interest):
            savings_interest = float(savings_interest)
            break
        else:
            print("Interest rate must be a number.")

    while True:
        savings_maturity = input("Enter number of months: ")
        if savings_maturity.isdigit():
            savings_maturity = int(savings_maturity)
            break
        else:
            print("Months must be a numeric whole number.")

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = savings_account.create_savings_account(savings_balance, savings_interest, savings_maturity)
  
    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Your savings account earned ${interest_earned:.2f} in interest and your new balance is ${updated_savings_balance:.2f}.")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    while True:
        cd_balance = input("Enter CD balance: ")
        if is_float(cd_balance):
            cd_balance = float(cd_balance)
            break
        else:
            print("CD Balance must be a number.")

    while True:
        cd_interest = input("Enter interest rate: ")
        if is_float(cd_interest):
            cd_interest = float(cd_interest)
            break
        else:
            print("Interest rate must be a number.")

    while True:
        cd_maturity = input("Enter number of months: ")
        if cd_maturity.isdigit():
            cd_maturity = int(cd_maturity)
            break
        else:
            print("Months must be a numeric whole number.")

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = cd_account.create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Your CD account earned ${interest_earned:.2f} in interest and your new balance is ${updated_cd_balance:.2f}.")

# Checks whether the entry is a float, isdigit was failing when entering numbers
# with a decimal place, so I cam up with this simple method    
def is_float(n):
    try:
        float(n)
        return True
    except:
        return False
            
if __name__ == "__main__":
    # Call the main function.
    main()
