import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")

    secret_number = random.randint(1, 100)

    attempts = 0
    max_attempts = 7

    while attempts < max_attempts:
        try:
            guess = int(input("\nEnter your guess: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            break

        print(f"Attempts left: {max_attempts - attempts}")

    else:
        print(f"\nGame Over! The correct number was {secret_number}")

    print("Thanks for playing!")


if __name__ == "__main__":
    number_guessing_game()
