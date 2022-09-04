import random
from words import word_list

# This section will import a random word from words.py
word = random.choice(word_list)

correct = []
incorrect = []
letters_guessed = []
current_guessed = 0
