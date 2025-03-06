# Word Scramble Game

## Overview

The **Word Scramble Game** is a GUI-based application built using the `breezypythongui` library. The game selects a random word from a predefined list, scrambles it, and presents it to the user. The user has three attempts to guess the correct word. Points are awarded based on the length of the word, multiplied by 10, for each correct guess. After each round, the user can choose to continue playing or exit the game.

## Features

- **Random Word Selection**: The game selects a random word from a predefined list stored in a text file (`words.txt`).
- **Word Scrambling**: The selected word is scrambled and displayed to the user.
- **User Interaction**: The user can input their guess and check if it matches the original word.
- **Feedback System**: The game provides feedback after each guess, indicating whether the guess was correct or not.
- **Score Tracking**: Points are awarded based on the length of the word, multiplied by 10, for each correct guess.
- **Multiple Attempts**: The user has three attempts to guess the correct word.
- **Continue Option**: After each round, the user can choose to continue playing or exit the game.

## Requirements

- Python 3.x
- `breezypythongui` library

## Installation

1. **Install Python**: Ensure that Python 3.x is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install `breezypythongui`**:
   - You can install the `breezypythongui` library using pip:
     ```bash
     pip install breezypythongui
     ```

3. **Download the Game Files**:
   - Clone or download the repository containing the game files.
   - Ensure that the `words.txt` file is in the same directory as the game script. The `words.txt` file should contain a list of words separated by commas.

## How to Play

1. **Start the Game**:
   - Run the `WordScrambleGame.py` script.
   - Click the "Start" button to begin a new game round.

2. **Guess the Word**:
   - A scrambled word will be displayed in the "Scrambled Word" field.
   - Enter your guess in the "Your Guess" field and click the "Check" button.

3. **Receive Feedback**:
   - If your guess is correct, you will receive a congratulatory message, and your score will be updated.
   - If your guess is incorrect, you will be informed, and the number of remaining attempts will be decremented.

4. **Continue or Exit**:
   - After each round, you can choose to continue playing by entering "Y" in the "Continue (Y/N)" field and clicking the "Continue" button.
   - To exit the game, enter "N" in the "Continue (Y/N)" field and click the "Continue" button.

## Code Structure

- **WordScrambleGame Class**:
  - The main class that handles the GUI and game logic.
  - Methods include:
    - `__init__`: Initializes the GUI components and game variables.
    - `readAndScramble`: Reads words from `words.txt` and scrambles a randomly selected word.
    - `startGame`: Starts a new game round.
    - `checkGuess`: Checks the user's guess and updates the game state.
    - `keepOnPlaying`: Handles the continuation or exit logic.

## Example `words.txt` File

The `words.txt` file should contain a list of words separated by commas. For example:

## Screenshots

![Word Scramble Game Screenshot](screenshot.png)

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any suggestions or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the creators of the `breezypythongui` library for making GUI development in Python more accessible.
- Special thanks to all contributors and users of the game.

## Contact

For any questions or feedback, please contact [Your Name] at [your.email@example.com].

---

Enjoy playing the **Word Scramble Game**! 🎮
