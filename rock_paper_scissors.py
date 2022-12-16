import random

exit = False
user_points = 0
computer_points = 0

while exit == False:
    options = ['rock', 'paper', 'scissors']
    user_input = input('Enter rock, paper, scissors or exit: ')
    computer_input = random.choice(options)

    if user_input == 'exit':
        print('Game ended')
        print(f'User has {user_points} points and computer has {computer_points} points.')
        if user_points > computer_points:
            print('You are the final winner!')
        elif user_points < computer_points:
            print('The final winner is computer!')
        else:
            print('We have two winners!')
        exit = True
    elif user_input == 'rock':
        if computer_input == 'rock':
            print(f'User entered {user_input} and computer chose {computer_input}')
            print('It is a tie!')
        elif computer_input == 'paper':
            print(f'User entered {user_input} and computer chose {computer_input}')
            print('Computer wins!')
            computer_points += 1
        elif computer_input == 'scissors':
            print(f'User entered {user_input} and computer chose {computer_input}')
            print('You win!')
            user_points += 1
    elif user_input == 'paper':
        if computer_input == 'rock':
            print(f'User entered {user_input} and computer chose {computer_input}')
            print('You win!')
            user_points += 1
        elif computer_input == 'paper':
            print(f'User entered {user_input} and computer chose {computer_input}')
            print('It is a tie!')
        elif computer_input == 'scissors':
            print(f'User entered {user_input} and computer chose {computer_input}')
            print('Computer wins!')
            computer_points += 1
    elif user_input == 'scissors':
        if computer_input == 'rock':
            print(f'User entered {user_input} and computer chose {computer_input}')
            print('Computer wins!')
            computer_points += 1
        elif computer_input == 'paper':
            print(f'User entered {user_input} and computer chose {computer_input}')
            print('You win!')
            user_points += 1
        elif computer_input == 'scissors':
            print(f'User entered {user_input} and computer chose {computer_input}')
            print('It is a tie!')

