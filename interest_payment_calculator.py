def calculator():
    print('This is a monthly payment loan calculator\n')

    principal = float(input('What is the loan amount: '))
    annual_interest_rate = float(input('What is the annual interest rate: '))
    years = int(input('How long is the loan period in years: '))

    monthly_interest_rate = annual_interest_rate / 1200
    number_of_months = years * 12
    monthly_payment = principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-number_of_months))

    print('The monthly payment for this loan is: %.2f' % monthly_payment)

calculator()