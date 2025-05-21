"""
Snowman game logic module.

Contains the main game loop and supporting functions for the Snowman word guessing game.
"""

import random
import ascii_art as aa
from typing import List


# List of possible secret words
WORDS: List[str] = ["python", "git", "github", "snowman", "meltdown"]

# Maximum allowed wrong guesses before game over
max_mistakes: int = 4

# ANSI escape sequences for colored output
GREEN: str = "\033[92m"
RED: str = "\033[91m"
RESET: str = "\033[0m"
BLUE: str = "\033[94m"


def get_random_word() -> str:
    """
    Select a random word from the WORDS list.

    Returns:
        A random secret word as a string.
    """
    return WORDS[random.randint(0, len(WORDS) - 1)]


def clear_screen() -> None:
    """
    Clears the console screen by printing several newlines.
    """
    print("\n" * 100)


def display_game_state(mistakes: int, secret_word: str, guessed_letters: List[str]) -> None:
    """
    Display the current state of the game including the snowman ASCII art
    for the current number of mistakes and the progress on the secret word.

    Args:
        mistakes: Number of incorrect guesses made.
        secret_word: The word the player is trying to guess.
        guessed_letters: List of letters the player has guessed so far.
    """
    if mistakes < max_mistakes:
        print(aa.STAGES[mistakes])

    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print(f"{BLUE}Word: {display_word}{RESET}\n")


def run_single_game() -> None:
    """
    Run a single round of the Snowman game.
    Handles input validation, game state updates, and win/lose conditions.
    """
    secret_word: str = get_random_word()
    guessed_letters: List[str] = []
    mistakes: int = 0

    print("Welcome to Snowman Meltdown!")
    clear_screen()
    display_game_state(mistakes, secret_word, guessed_letters)

    while True:
        guess: str = input("Guess a letter: ").lower()

        # Validate input: must be a single alphabetical character
        while len(guess) != 1 or not guess.isalpha():
            guess = input(f"{RED}Input must be a single letter! Guess again please: {RESET}").lower()

        print("You guessed:", guess)

        if guess in guessed_letters:
            print(f"{RED}You already guessed that letter. Try another one.{RESET}")
            continue

        if guess in secret_word:
            guessed_letters.append(guess)
            clear_screen()
            display_game_state(mistakes, secret_word, guessed_letters)
            print(f"{GREEN}Good guess!{RESET}")
        else:
            mistakes += 1
            clear_screen()
            display_game_state(mistakes, secret_word, guessed_letters)
            print(f"{RED}Wrong guess!{RESET}")

        # Check for win condition
        if all(char in guessed_letters for char in secret_word):
            print(f"{GREEN}{aa.YOU_WIN}{RESET}")
            break

        # Check for lose condition
        if mistakes >= max_mistakes:
            print(f"{RED}{aa.GAME_OVER}{RESET}")
            print(f"{RED}The word was: {secret_word}.{RESET}")
            break


def play_game() -> None:
    """
    Play the Snowman game repeatedly until the player decides to quit.
    """
    while True:
        run_single_game()
        answer: str = input("Do you want to play again? (y/n): ").strip().lower()
        if answer != "y":
            print("Okay, bye, till next time!")
            break
