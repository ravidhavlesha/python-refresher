from random import choice

user_wins = 0
computer_wins = 0

options = ['rock', 'paper', 'scissors']
winning_conditions = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}


def determine_winner(user_input, computer_input):
    global user_wins, computer_wins
    if user_input == computer_input:
        print("Draw")
    elif winning_conditions[user_input] == computer_input:
        print("User wins!")
        user_wins += 1
    else:
        print("Computer wins!")
        computer_wins += 1


while True:
    user_input = input('Choose Rock/Paper/Scissors or Q to quit: ').lower()
    if user_input == 'q':
        break

    if user_input not in options:
        print(f"Invalid input: {user_input}")
        continue

    computer_input = choice(options)

    print(f"User: {user_input}")
    print(f"Computer: {computer_input}")

    determine_winner(user_input, computer_input)

print(f"Result:\nComputer: {computer_wins}\nUser: {user_wins}")
print("Game over!")
