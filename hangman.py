import random

#This section is to let player add their name
#name = input("ENTER YOUR NAME >> ").upper()
#print("WELCOME", name, "LETS PLAY HANGMAN...")

# This section will import a random word from words.py
word_list = ["internet", "camera"]

word = random.choice(word_list).upper()

# These will collect number of correct, incorrect etc
correct = ['_'] * len(word)
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

# While loop for hangman

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
            print("Letter guessed: ",(user_guess))
        else:
            print("YOU HAVE ALREADY GUESSED THAT")
        print(incorrect)
    
    if len(incorrect) > 7:
        print("*GAME OVER*")
        print("YOU'VE KILLED HIM... THE WORD WAS:", word,)
        break
    if '_' not in correct:
        print("HuRrAyYy!!! WELL DONE!")
        print("-+-----------")
        print(" | *YOU SAVED*  ")
        print(" |    *ME*   ")
        print(" |    \O/    ")
        print(" |     |     ")
        print("===   / \    ")
        break
