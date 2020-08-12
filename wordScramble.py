"""
Md Islam

This programs creates a GUI based "Word Scramble" game.
It picks a random word from the list, scrambles it, and
shows it to the user. The user gets three chances to
guess and option to continue playing after each round.
It also gives the user points based on the length of the
word times 10 per correct guess.

"""
# Using EasyFrame for the GUI
from breezypythongui import EasyFrame
# random library to scramble and pick a random word
import random


class WordScrambleGame(EasyFrame):
	# Initializer
	def __init__(self):
		# Title and the background color
		EasyFrame.__init__(self, title="Word Scramble Game", background="blue")

		# Start button to start the game
		self.button = self.addButton(text="Start", row=0, column=0, columnspan=2, command=self.readAndScramble)

		# Shows the scrambled word to the user
		self.addLabel(text="Scramble Word", row=1, column=0, background="orange")
		self.scrambleWord = self.addTextField(text="", row=1, column=1, state="readonly")

		# Takes the user guess to check if it's correct or not
		self.addLabel(text="Your Guess", row=2, column=0, background="orange")
		self.userGuess = self.addTextField(text="", row=2, column=1)

		# Button to check if the guesses are are correct or not
		self.button = self.addButton(text="Check", row=3, column=0, columnspan=2, command=self.game)

		# Display message after each guess and round
		self.addLabel(text="Message", row=4, column=0, background="orange")
		self.feedback = self.addTextField(text="", row=4, column=1, state="readonly")

		# Display the original word, after each round, if the three guesses were incorrect
		self.addLabel(text="Original Word", row=5, column=0, background="orange")
		self.originalWord = self.addTextField(text="", row=5, column=1, state="readonly")

		# Display how many chances are left out of three
		self.addLabel(text="Chances left", row=6, column=0, background="orange")
		self.chanceLeft = self.addIntegerField(value=3, row=6, column=1)

		# Display the total score after each round
		self.addLabel(text="Total Score", row=7, column=0, background="orange")
		self.totalScore = self.addIntegerField(value=0, row=7, column=1)

		# Offer the user option to continue playing
		self.addLabel(text="Do you want to continue(Y/N)", row=8, column=0, background="orange")
		self.continuation = self.addTextField(text="", row=8, column=1)

		# Button to keep playing
		self.button = self.addButton(text="Continue", row=9, column=0, columnspan=2, command=self.keepOnPlaying)

	#  Reads the words from the text file and scrambles it
	def readAndScramble(self):
		# Reading words from text file
		textInput = []
		infile = open("words.txt", "r")
		for line in infile:
			textInput = line.split(",")

		# choosing a random word to scramble
		word = random.choice(textInput)

		""" 
		This portion of the code was given by 
		course instructor, Seyed Ziae Mousavi Mojab.
		"""
		word_list = list(word)
		random.shuffle(word_list)
		scrambled = ''.join(word_list)
		self.scrambleWord.setText(scrambled)
		return word

	def game(self):
		# Random word from the function readAndScramble()
		correctWord = self.readAndScramble()

		# User guess
		guess = self.userGuess.getText()

		totalPoint = 0
		chance = 3
		rightMessage = "Congratulation, you won!"
		wrongMessage = "Sorry, you didn’t win"
		text = "Wrong! Try Again"

		"""
		Checing if the user guess is correct and 
		displaying message and earned points 
		"""
		if guess == correctWord:
			self.feedback.setText(rightMessage)
			totalPoint = len(correctWord) * 10
			self.totalScore.setNumber(totalPoint)
		else:
			"""
			Giving three chances to the user to make 
			a correct guess and displaying a interactive
			message after each user guess. 
			"""
			while chance != 1:
				chance -= 1
				self.chanceLeft.setNumber(chance)
				self.feedback.setText(text)
				guess = self.userGuess.getText()

		"""
		Displaying the error message, earned points,
		and the original word after each round. 
		"""
		self.feedback.setText(wrongMessage)
		self.totalScore.setNumber(totalPoint)
		self.originalWord.setText(correctWord)

	# Option to continue playing or exit
	def keepOnPlaying(self):
		confirmation = self.continuation.getText()
		if confirmation == "Y":
			self.game()
		else:
			exit()


WordScrambleGame().mainloop()




