# Mortgage calculation function
def calculate_monthly_payment(loan_amount, annual_interest_rate, loan_term_years):
    # Convert annual interest rate to monthly rate
    monthly_interest_rate = annual_interest_rate / 12 / 100
    
    # Calculate the number of monthly payments
    num_payments = loan_term_years * 12
    
    # Calculate the monthly mortgage payment
    monthly_payment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate)**num_payments) / ((1 + monthly_interest_rate)**num_payments - 1)
    
    return monthly_payment

# Input parameters
loan_amount = 300000  # Example loan amount in dollars
annual_interest_rate = 4.5  # Example annual interest rate (in percentage)
loan_term_years = 30  # Example loan term in years

# Calculate and print the monthly mortgage payment
monthly_payment = calculate_monthly_payment(loan_amount, annual_interest_rate, loan_term_years)
print(f"The monthly mortgage payment is: ${monthly_payment:.2f}")