"""
Entry point for the Snowman game.

This script imports the game logic module and starts the game.
"""

import game_logic as gl


def main() -> None:
    """
    Start the Snowman game by calling the play_game function from the game_logic module.
    """
    gl.play_game()


if __name__ == "__main__":
    main()

