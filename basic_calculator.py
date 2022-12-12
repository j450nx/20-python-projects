# define the functions needed: add, sub, mul, div
# print options for the user
# ask for the value
# call the corresponding function
# while loop to continue the program until the user wants to exit

def add(a, b):
    answer = a + b
    print(f'{a} + {b} = {answer}\n')

def sub(a, b):
    answer = a - b
    print(f'{a} - {b} = {answer}\n')

def mul(a, b):
    answer = a * b
    print(f'{a} * {b} = {answer}\n')

def div(a, b):
    answer = a / b
    print(f'{a} / {b} = {answer}\n')

while True:
    print('A. Addition')
    print('B. Subjection')
    print('C. Multiplication')
    print('D. Division')
    print('E. Exit')
    # a list of constrained options the user can enter from
    options = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E']

    while True:
        try:
            choice = input('Input your choice: ')
        except ValueError:
            continue
        # if user input is not one of the options, continue with request
        if choice not in options:
            print('\nEnter a valid choice!')
            print('A. Addition')
            print('B. Subjection')
            print('C. Multiplication')
            print('D. Division')
            print('E. Exit')
        else:
            break

    if choice == 'a' or choice == 'A':
        print('Addition')
        # while loop to check whether user input is an integer
        while True:
            try:
                a = int(input('Input first number: '))
            except ValueError:
                continue
            if isinstance(a, int):
                break
        while True:
            try:
                b = int(input('Input second number: '))
            except ValueError:
                continue
            if isinstance(b, int):
                break
        add(a, b)
    elif choice == 'b' or choice == 'B':
        print('Subtraction')
        while True:
            try:
                a = int(input('Input first number: '))
            except ValueError:
                continue
            if isinstance(a, int):
                break
        while True:
            try:
                b = int(input('Input second number: '))
            except ValueError:
                continue
            if isinstance(b, int):
                break
        sub(a, b)
    elif choice == 'c' or choice == 'C':
        print('Multiplication')
        while True:
            try:
                a = int(input('Input first number: '))
            except ValueError:
                continue
            if isinstance(a, int):
                break
        while True:
            try:
                b = int(input('Input second number: '))
            except ValueError:
                continue
            if isinstance(b, int):
                break
        mul(a, b)
    elif choice == 'd' or choice == 'D':
        print('Division')
        while True:
            try:
                a = int(input('Input first number: '))
            except ValueError:
                continue
            if isinstance(a, int):
                break
        while True:
            try:
                b = int(input('Input second number: '))
            except ValueError:
                continue
            if isinstance(b, int):
                break
        div(a, b)
    elif choice == 'e' or choice == 'E':
        print('Good bye')
        quit()