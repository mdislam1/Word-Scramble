"""
This program creates a GUI-based "Word Scramble" game.  
It selects a random word from a predefined list, scrambles it, and displays it to the user.  
The user has three attempts to guess the correct word. Points are awarded based on the word's length, multiplied by 10, for each correct guess.  
After each round, the user can choose to continue playing or exit the game.  
"""

# Using EasyFrame for the GUI
from breezypythongui import EasyFrame
import random


class WordScrambleGame(EasyFrame):
    # Initializer
    def __init__(self):
        EasyFrame.__init__(self, title="Word Scramble Game", background="blue")

        # Start button to start the game
        self.button = self.addButton(text="Start", row=0, column=0, columnspan=2, command=self.startGame)

        # Shows the scrambled word to the user
        self.addLabel(text="Scrambled Word", row=1, column=0, background="orange")
        self.scrambleWord = self.addTextField(text="", row=1, column=1, state="readonly")

        # Takes the user's guess
        self.addLabel(text="Your Guess", row=2, column=0, background="orange")
        self.userGuess = self.addTextField(text="", row=2, column=1)

        # Button to check if the guess is correct
        self.checkButton = self.addButton(text="Check", row=3, column=0, columnspan=2, command=self.checkGuess)

        # Display message after each guess
        self.addLabel(text="Message", row=4, column=0, background="orange")
        self.feedback = self.addTextField(text="", row=4, column=1, state="readonly")

        # Display the original word after three incorrect guesses
        self.addLabel(text="Original Word", row=5, column=0, background="orange")
        self.originalWord = self.addTextField(text="", row=5, column=1, state="readonly")

        # Display remaining chances
        self.addLabel(text="Chances Left", row=6, column=0, background="orange")
        self.chanceLeft = self.addIntegerField(value=3, row=6, column=1)

        # Display total score
        self.addLabel(text="Total Score", row=7, column=0, background="orange")
        self.totalScore = self.addIntegerField(value=0, row=7, column=1)

        # Offer the option to continue playing
        self.addLabel(text="Continue (Y/N)", row=8, column=0, background="orange")
        self.continuation = self.addTextField(text="", row=8, column=1)

        # Button to continue playing
        self.continueButton = self.addButton(text="Continue", row=9, column=0, columnspan=2, command=self.keepOnPlaying)

        # Initialize game variables
        self.word = ""
        self.scrambled = ""
        self.chances = 3
        self.totalPoints = 0

    # Reads words from a file and scrambles a randomly selected word
    def readAndScramble(self):
        try:
            with open("words.txt", "r") as infile:
                words = infile.read().strip().split(",")

            word = random.choice(words).strip()
            scrambled = "".join(random.sample(word, len(word)))
            return word, scrambled
        except FileNotFoundError:
            self.feedback.setText("Error: words.txt not found.")
            return "", ""

    # Start a new game round
    def startGame(self):
        self.word, self.scrambled = self.readAndScramble()
        if self.word:
            self.scrambleWord.setText(self.scrambled)
            self.originalWord.setText("")
            self.feedback.setText("")
            self.chanceLeft.setNumber(3)
            self.chances = 3
        else:
            self.scrambleWord.setText("")

    # Check the user's guess
    def checkGuess(self):
        guess = self.userGuess.getText().strip()

        if guess == self.word:
            self.feedback.setText("Congratulations, you won!")
            self.totalPoints += len(self.word) * 10
            self.totalScore.setNumber(self.totalPoints)
            self.originalWord.setText(self.word)
        else:
            self.chances -= 1
            self.chanceLeft.setNumber(self.chances)
            if self.chances > 0:
                self.feedback.setText("Wrong! Try Again")
            else:
                self.feedback.setText("Sorry, you didn't win")
                self.originalWord.setText(self.word)

    # Option to continue playing or exit
    def keepOnPlaying(self):
        confirmation = self.continuation.getText().strip().upper()
        if confirmation == "Y":
            self.startGame()
        else:
            self.quit()


# Run the game
WordScrambleGame().mainloop()
