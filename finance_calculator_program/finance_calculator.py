def calculate_simple_interest():
    principal = float(input("Enter the principal:"))
    rate = float(input("Enter the rate:"))
    time_period = float(input("Enter the time period:"))
    simple_interest = (principal * rate * time_period)
    print(f"The simple interest is: ${simple_interest}")


def calculate_compound_interest():
    initial_deposit = float(input("Enter your initial deposit:"))
    interest_rate = float(input("Enter your interest rate:"))
    paid_interest = float(input("Enter your paid interest:"))
    years = float(input("Enter how many years the money are invested:"))
    final_value_of_savings = initial_deposit * (1 + interest_rate/paid_interest) ** (paid_interest*years)
    print(f"The compound interest is: {final_value_of_savings - initial_deposit}")


def calculate_loan_interest():
    principal = float(input("Enter your principal:"))
    rate = float(input("Enter your rate:"))
    tenure = float(input("Enter your tenure:"))
    interest = principal * rate * tenure
    print(f"The loan interest is: {interest}")


def calculate_future_value_savings():
    investment_amount = float(input("Enter your investment amount:"))
    number_rate = float(input("Enter your number rate:"))
    number_years = float(input("Enter the years to calculate the savings:"))
    future_value = investment_amount * (1 + number_rate) ** number_years
    print(f"The future value will be: {future_value}")


while True:
    print("Welcome to the finance calculator")
    print("1. Calculate Simple Interest")
    print("2. Calculate Compound Interest")
    print("3. Calculate Loan Interest")
    print("4. Calculate Future Value of Savings")
    print("5. Quit")

    choice = int(input("Enter a operation to do (1/2/3/4/5):"))
    if choice == 1:
        calculate_simple_interest()
    elif choice == 2:
        calculate_compound_interest()
    elif choice == 3:
        calculate_loan_interest()
    elif choice == 4:
        calculate_future_value_savings()
    elif choice == 5:
        print("Goodbye...!")
        break
    else:
        print("Invalid operation.Please enter a number 1, 2, 3, 4 or 5!")


