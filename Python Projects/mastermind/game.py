"""
This is Mastermind!

The game involves guessing a secret code of colors within a certain number of tries.
The player needs to guess the correct colors in the correct positions to win the game.

Functions:
- generate_code: Generate a random code from a list of colors.
- guess_code: Ask the user for their guess and validate it.
- check_code: Check the guess against the real code and return the result.
- game: Run the game.

Constants:
- COLORS: A list of valid colors.
- TRIES: The number of tries allowed to guess the code.
- CODE_LENGTH: The length of the secret code.
"""
import random  # Importing the random module to generate a random code.


COLORS = ["R", "G", "B", "Y", "W", "O"]  # The valid colors for the game.

TRIES = 10  # The number of tries allowed to guess the code.

CODE_LENGTH = 4  # The length of the secret code.


def generate_code():
    """Generate a random code from the list of colors."""
    code = []
    for _ in range(CODE_LENGTH):
        color = random.choice(
            COLORS
        )  # Randomly choosing a color from the list of colors.
        code.append(color)  # Adding the color to the code.

    return code


def guess_code():
    """Ask user for their guess and validate it."""
    while True:  # Looping until the user enters a valid guess.
        guess = (
            input("What is your Guess: ").upper().split(" ")
        )  # Asking the user for their guess and converting it to uppercase.

        if (
            len(guess) != CODE_LENGTH
        ):  # Checking if the length of the guess is equal to the length of the code.
            print(f"You must guess {CODE_LENGTH} colors.")
            continue  # Restarting the loop if the user enters an invalid guess.

        for color in guess:
            if color not in COLORS:
                print(
                    f"Invalid color: {color}. Try again!"
                )  # Checking if the user has entered a valid color.
                break
        else:
            break  # Breaking out of the loop if the user enters a valid guess.

    return guess


def check_code(guess, real_code):
    """Check the guess against the real code and return the result."""
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    for (
        color
    ) in real_code:  # Counting the number of times each color appears in the code.
        if color not in color_counts:  # If the color is not in the dictionary, add it.
            color_counts[color] = 0  # Setting the count of the color to 0.
        color_counts[color] += 1  # Incrementing the count of the color.

    for guess_color, real_code in zip(guess, real_code):  # Checking for correct pos.
        if guess_color == real_code:  # If the color is in the correct position.
            correct_pos += 1  # Incrementing the correct position count.
            color_counts[guess_color] -= 1  # Decrementing the color count.

    for guess_color in zip(guess, real_code):  # Checking for incorrect pos.
        if (
            guess_color in color_counts and color_counts[guess_color] > 0
        ):  # If the color is in the code.
            incorrect_pos += 1
            color_counts[guess_color] -= 1  # Decrementing the color count.

    return correct_pos, incorrect_pos


def game():
    """Run the game."""

    print("Welcome to Mastermind!")
    print(f"You have {TRIES} tries to guess the code....")
    print("The valid colors are: ", *COLORS)

    code = generate_code()
    for attempts in range(1, TRIES + 1):  # Looping until the user runs out of tries.
        guess = guess_code()  # Asking the user for their guess.
        correct_pos, incorrect_pos = check_code(guess, code)  # Checking the guess.

        if correct_pos == CODE_LENGTH:  # If the user guesses the code.
            print(f"You guessed the code in {attempts} tries!")
            break  # Breaking out of the loop.

        print(
            f"Correct Positions: {correct_pos} | Incorrect Positions: {incorrect_pos}"
        )
    else:  # If the user runs out of tries.
        print("You ran out of tries!, the code was:", *code)


if __name__ == "__main__":  # If the file is run directly.
    game()  # Running the game.
