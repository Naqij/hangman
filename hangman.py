import random
from words import words_list

def hangman():
    word = random.choice(words_list)
    while '-' in word or ' ' in word:
        word = random.choice(words_list)

    print(word)

hangman()