import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

max_mistakes = 4

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"
BLUE = "\033[94m"


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]



def clear_screen():
    print("\n" * 100)


def display_game_state(mistakes, secret_word, guessed_letters):
    # Display the snowman stage for the current number of mistakes.
    if mistakes < max_mistakes:
        print(STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print(f"{BLUE}Word: {display_word}{RESET}")
    print("\n")


def run_single_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")
    clear_screen()
    display_game_state(mistakes, secret_word, guessed_letters)

    while True:
        guess = input("Guess a letter: ").lower()

        # Eingabe prüfen - solange neu fragen, bis valide
        while len(guess) != 1 or not guess.isalpha():
            guess = input(RED+"Input must be a single letter! Guess again please: "+RESET).lower()

        print("You guessed:", guess)

        if guess in guessed_letters:
            print(RED+"You already guessed that letter. Try another one."+RESET)
            continue

        if guess in secret_word:
            guessed_letters.append(guess)
            clear_screen()
            display_game_state(mistakes, secret_word, guessed_letters)
            print(GREEN+"Good guess!"+RESET)
        else:
            mistakes += 1
            clear_screen()
            display_game_state(mistakes, secret_word, guessed_letters)
            print(RED+"Wrong guess!"+RESET)

        if all(char in guessed_letters for char in secret_word):
            print(GREEN+"You saved the snowman!"+RESET)
            break

        if mistakes >= max_mistakes:
            print(f"{RED}Game over! The word was: {secret_word}.{RESET}")
            break


def play_game():
    while True:
        run_single_game()
        answer = input("Do you want to play again? (y/n): ").strip().lower()
        if answer != "y":
            print("Okay, bis zum nächsten Mal!")
            break

