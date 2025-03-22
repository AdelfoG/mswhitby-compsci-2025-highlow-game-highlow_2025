import random

def guess_my_number():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Welcome to 'Guess My Number'!")
    print("I have picked a number between 1 and 100. Try to guess it!")

    while True:
        # Get the player's guess
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        attempts += 1

        # Check the player's guess
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
            break

# Start the game
if __name__ == "__main__":
    guess_my_number()
