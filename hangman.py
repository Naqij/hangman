import random
from words import word_list

# This section will import a random word from words.py
word = random.choice(word_list)

# These will collect number of correct, incorrect etc
correct = []
incorrect = []
letters_guessed = []
current_guessed = 0

def update():
    for x in correct:
        print(x, end=' ')
    print()

update()
