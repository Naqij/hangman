import random
from words import word_list

# This section is to let player add their name
name = input("ENTER YOUR NAME >> ").upper()
print("\nWELCOME", name, "LETS PLAY HANGMAN...\n")


# This section will import a random word from words.py

word = random.choice(word_list).upper()

# Function to let player know how many letters are in the word

print("The word has", len(word), "letters\n")

# These will collect number of correct, incorrect etc.
correct = ['_'] * len(word)
incorrect = []
letters_guessed = []
current_guessed = 0


def update():
    for x in correct:
        print(x, end = ' ')
    print()

# Hangman to be printed if wrong answers are given


def hangman(tries):
    if (tries == 1):
        print("\n7 tries left")
        print("-+-----------")
        print(" |    O      ")
        print(" |           ")
        print(" |           ")
        print("===          ")

    elif (tries == 2):
        print("\n6 tries left")
        print("-+-----------")
        print(" |   O       ")
        print(" |   |       ")
        print(" |           ")
        print("===          ")
      
    elif (tries == 3):
        print("\n5 tries left")
        print("-+-----------")
        print(" |   O       ")
        print(" |   |       ")
        print(" |  /        ")
        print("===          ")
      
    elif (tries == 4):
        print("\n4 tries left")
        print("-+-----------")
        print(" |   O       ")
        print(" |   |       ")
        print(" |  / \      ")
        print("===          ")

    elif (tries == 5):
        print("\n3 tries left")
        print("-+-----------")
        print(" |  \O       ")
        print(" |   |       ")
        print(" |  / \      ")
        print("===          ")
      
    elif (tries == 6):
        print("\n2 tries left")
        print("-+-----------")
        print(" |  \O/      ")
        print(" |   |       ")
        print(" |  / \      ")
        print("===          ")

    elif (tries == 7):
        print("\n1 try left")
        print("-+-----------")
        print(" |   |       ")
        print(" |  \O/      ")
        print(" |   |       ")
        print(" |  / \      ")
        print("===          ")
      
    elif (tries == 8):
        print("\n-+---+-------")
        print("   |   |       ")
        print("   |   +O      ")
        print("   | / | \     ")
        print("   |  / \      ")
        print("  ===          ")


# While loop for hangman
# Codes below will go around the entire 
## code as many times as needed to complete the game

while True:

    user_guess = input("Guess a Letter: ").upper()

    if user_guess in word:
        counter = 0
        for x in word:
            if x == user_guess:
                correct[counter] = user_guess
            counter += 1
        update()
    else:
        if user_guess not in incorrect:
            incorrect.append(user_guess)
            hangman(len(incorrect))
            print("\nLetter guessed: ",(user_guess))
        else:
            print("\nYOU HAVE ALREADY GUESSED THAT")
        print(incorrect)

    if len(incorrect) > 7:
        print("\nGAME OVER")
        print("YOU'VE KILLED HIM... THE WORD WAS:", word,"\n")
        break

    if '_' not in correct:
        print("HuRrAyYy!!! WELL DONE!")
        print("\n-+-----------")
        print("   |  YOU SAVED  ")
        print("   |     ME    ")
        print("   |    \O/    ")
        print("   |     |     ")
        print("  ===   / \    ")
        break
