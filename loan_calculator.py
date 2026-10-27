# Input personal details
full_name = input("Enter full name: ").upper()
age = int(input("Enter your age: "))
employment_status = input("Are you employed (Yes/No): ").lower()
montly_income = int(input("Enter your montly income: N"))

# Fill loan details
requested_loan_amount = int(input("Enter loan amount: N"))
loan_term = int(input("Enter loan term(monthly): "))

# Calculate the interest
interest  = requested_loan_amount * 0.12 * (loan_term/12)
  
# Calculate the total repayment
total_repayment = requested_loan_amount + interest

# Calculate montly installment
montly_installment = total_repayment / loan_term

if age <= 18 or age > 80 : # Checks if the user is above or below age requirement
    print() # Leave one line
    print("Rejected: Age not acceptable.")
elif employment_status != "yes".lower(): # Checks if the user is employed or not
    print("Rejected: Must be employed.")
elif montly_income < 100000 : # Checks if the user's income is below or above  the minimum 
       print()
       print("Rejected: Income below minimum.")
elif requested_loan_amount <= 0 or (requested_loan_amount > (montly_income * 3)): # Checks if loan is above 0 or loan is 3 times montly income
    print()
    print("Rejected: Loan amount must be greater than zero \nand no more than 3 times monthly income.")
elif loan_term != 6 and loan_term != 12: # Accepts only 6 and 12 loan terms 
    print("Rejected: unsupported term.")   
else:
    # Display output
    print("-" * 60)
    print(f"Congratulations!! Mr {full_name}, Loan Approved.")
    print(f"Interest: NGN{interest}") 
    print(f"Total Repayment: NGN{total_repayment}")
    print(f"Montly installment: NGN{montly_installment}") 
    print("-" * 60) 
        