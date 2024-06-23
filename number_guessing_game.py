import random

def get_valid_guess(prompt):
    while True:
        guess = int(input(prompt))
        if 1 <= guess <= 10:
            return guess
        else:
            print("Error: Please enter a number between 1 and 10.")

def start_game():
    n = random.randint(1, 10)
    guess = get_valid_guess("Enter any number between 1 and 10: ")

    while n != guess:
        if guess < n:
            print("Too low")
        else:
            print("Too high!")
        
        guess = get_valid_guess("Enter number again between 1 and 10: ")

    print("You guessed it right!!")
    if input('Want to try again? (y/n): ').lower() == 'y':
        start_game()

start_game()