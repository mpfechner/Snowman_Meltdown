import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

max_mistakes = 4

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
    print("Word: ", display_word)
    print("\n")


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")
    # For now, display the initial game state.
    clear_screen()
    display_game_state(mistakes, secret_word, guessed_letters)

    while True:
        guess = input("Guess a letter: ").lower()
        print("You guessed:", guess)

        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue

        if guess in secret_word:
            guessed_letters.append(guess)
            clear_screen()
            display_game_state(mistakes, secret_word, guessed_letters)
            print("Good guess!")
        else:
            mistakes += 1
            clear_screen()
            display_game_state(mistakes, secret_word, guessed_letters)
            print("Wrong guess!")

        # Prüfen, ob alle Buchstaben erraten wurden
        if all(char in guessed_letters for char in secret_word):
            print("You saved the snowman!")
            break

        # Optional: Abbruch, wenn zu viele Fehler
        if mistakes > max_mistakes:
            print(f"Game over! The word was: {secret_word}.")
            break

