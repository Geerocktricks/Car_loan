print("Enter Loan offered in USD:")
loan_amount = float(input())
print("Enter monthly slary:")
slary_earned = float(input())
print("Enter percentage of the salary paid:")
salary_paid = float(input())
def time_taken():
    print("You are expected to pay the loan over a period of " + str( loan_amount/(salary_paid/100 * slary_earned)) + " months")
time_taken()