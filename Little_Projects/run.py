'''
The game runner.
Author: MaliciousFiles (https://github.com/MaliciousFiles)
Contributor(s): mrmaxguns (https://github.com/mrmaxguns)

Currently supports:
* hangman
* guess the number
'''

# Imports
from hangman import hangman_game
from guess_the_number import num_game

# The title
title = 'Fun and classic games'

# Draw and "beautify" the title
print('-' * len(title))
print(title)
print('-' * len(title))

# Help menu
help = """

Help!
-----
Welcome to the help section. Here are basic instructions. Be sure to look at "README.md" and the "docs" folder for more info.

Basic operation:
* "q": quit
* "help": open this help menu thing
* "info": for info on the creators and how you can contribute

Games:
* "hangman" to play the classic hangman game
* "gtn" or "guess the number" to play guess the number

"""

# Info menu
info = """

Info
----
Some information about us:
Creator: MaliciousFiles (https://github.com/MaliciousFiles)
Contributors: mrmaxguns (https://github.com/mrmaxguns)

This is open source software. We would love you to contribute.
Just fork the repository (github.com/MaliciousFiles/Python-Projects).

"""

Playing = True

# Main loop
while Playing:
    # Print basic information
    print('\nType "help" to get help, "info" for info, "q" for quit or the name of the game you want to play!\n')

    # Get user input
    command = input('Your wish is my command: ').lower()

    # Run different commands depending on what the user said
    if command.startswith('q'):
        print('\nThanks for playing! See you next time.')
        quit()
    elif command == 'help':
        print(help)
    elif command == 'info':
        print(info)
    elif command.startswith('h'):
        print('Hangman!\n')

        while True:
            # Run hangman until user no longer wants to play
            hangman_game()
            again = input('Do you want to play again? y/n ')
            if again.lower().startswith('n'):
                print('\nThanks for playing hangman!')
                break
    elif command.startswith('g'):
        print('Guess the number!')

        # Run guess the number until the user no longer wants to play
        while True:
            level = input('Choose your level (easy/medium/hard/custom): ').lower()

            if level.startswith('e'):
                print('Level is easy\n')
                params = [40, 10]
            elif level.startswith('m'):
                print('Level is medium\n')
                params = [50, 5]
            elif level.startswith('h'):
                print('Level is hard\n')
                params = [100, 5]
            else:
                # Check to make sure the user chooses only natural numbers above 1
                while True:
                    try:
                        a = int(input('What is the maximum number of guessing? '))
                    except ValueError:
                        print('Invalid number!')
                        continue

                    if a > 1:
                        break

                    else:
                        print("Uh oh, that's an awfully small number! Try again")

                while True:
                    try:
                        b = int(input('What is the number of tries? '))
                    except ValueError:
                        print('Invalid number!')
                        continue

                    if b > 1:
                        break
                    else:
                        print("Uh oh, that's an awfully small number! Try again")

                print('You chose the range of 1 - %s and a maximum of %s tries\n' % (a, b))
                params = [a, b]

            # Run the actual game
            num_game(params[0], params[1])
            again = input('Do you want to play again? y/n ')
            if again.lower().startswith('n'):
                print('\nThanks for playing guess the number!')
                break
    else:
        # Invalid command
        print('Invalid Command')
        print('Please type help for a full list of commands')
