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

# Hangman to be printed if wrong answers are given
def hangman(tries):
    if (tries == 1):
        print("7 tries left")
        print("-+-----------")
        print(" |    O      ")
        print(" |           ")
        print(" |           ")
        print("===          ")

    elif (tries == 2):
        print("6 tries left")
        print("-+-----------")
        print(" |   O       ")
        print(" |   |       ")
        print(" |           ")
        print("===          ")
      
    elif (tries == 3):
        print("5 tries left")
        print("-+-----------")
        print(" |   O       ")
        print(" |   |       ")
        print(" |  /        ")
        print("===          ")
      
    elif (tries == 4):
        print("4 tries left")
        print("-+-----------")
        print(" |   O       ")
        print(" |   |       ")
        print(" |  / \      ")
        print("===          ")

    elif (tries == 5):
        print("3 tries left")
        print("-+-----------")
        print(" |  \O       ")
        print(" |   |       ")
        print(" |  / \      ")
        print("===          ")
      
    elif (tries == 6):
        print("2 tries left")
        print("-+-----------")
        print(" |  \O/      ")
        print(" |   |       ")
        print(" |  / \      ")
        print("===          ")

    elif (tries == 7):
        print("1 try left")
        print("-+-----------")
        print(" |   |       ")
        print(" |  \O/      ")
        print(" |   |       ")
        print(" |  / \      ")
        print("===          ")
      
    elif (tries == 8):
        print("-+---+-------")
        print(" |   |       ")
        print(" |   +O      ")
        print(" | / | \     ")
        print(" |  / \      ")
        print("===          ")


