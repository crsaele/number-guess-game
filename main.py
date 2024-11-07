# Imports the random module which will allow me to generate a random integer
import random


def number_guessing_game():
    # Sets the ranges for the random number in which it will be generated
    min_number = 1
    max_number = 100
    random_number = random.randint(min_number, max_number)

    print(f"Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {min_number} and {max_number}.")

    attempts = 0
    guessed_correctly = False

    
    while not guessed_correctly:
        # Get user input
        guess = input(f"Enter your guess: ")

        # Validate input
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue
 
        guess = int(guess)
        attempts += 1

        # Check the guess
        if guess < min_number or guess > max_number:
            print(f"Please guess a number within the range of {min_number} to {max_number}.")

        elif guess < random_number:
            print("Too low! Try again.")

        elif guess > random_number:
            print("Too high! Try again.")

        else:
            guessed_correctly = True
            print(f"Congratulations! You've guessed the number {random_number} in {attempts} attempts.")


# When the script is executed directly the code under this block will run
# If this script is imported as a module (file) to another module (file) it won't run
if __name__ == "__main__":
    # Run the game
    number_guessing_game()

