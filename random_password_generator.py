# Ask the user if they want to generate a random password
# If yes, ask for password length and generate password
# If no, exit program

import string
import random

characters = list(string.ascii_letters + string.digits + '!@#$%^&*()')

def generate_password():
    password_length = int(input('How long would you like the password to be: '))
    random.shuffle(characters)
    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = ''.join(password)

    print(f'The randomly generated password is ${password}')

option = input('Do you want to generate a password? (Yes/No): ')

if option == 'Yes' or option == 'yes':
    generate_password()
elif option == 'No' or option == 'no':
    print('Ending program')
    quit()
else:
    print('Invalid input, please input Yes or No')
    quit()
