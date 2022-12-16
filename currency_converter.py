def main():
    print('This program converts USD to Pounds Sterling\n')
    dollars = eval(input('Enter amount in dollars: '))
    pounds = convert_to_pounds(dollars)

    print(f'The amount is Pounds Sterling is ${pounds}')

convert_to_pounds = lambda dollars: dollars * 0.82

main()