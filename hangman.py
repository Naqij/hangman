import random
from words import words_list

def hangman():
    
def get_word(words):
    word = random.choice(words_list)
    print(word)

def print_hangman(wrong):
    if(wrong == 0):
        print("\n----------")
        print("   |")
        print("   |")
        print("   |")
        print("   |")
        print("  ---")

    elif(wrong == 1):
        print("\n-------+--")
        print("   |     O")
        print("   |")
        print("   |")
        print("   |")
        print("  ---")

    elif(wrong == 2):
        print("\n-------+--")
        print("   |     O")
        print("   |    /")
        print("   |")
        print("   |")
        print("  ---")

    elif(wrong == 3):
        print("\n-------+--")
        print("   |     O")
        print("   |    /")
        print("   |")
        print("   |")
        print("  ---")

    elif(wrong == 4):
        print("\n-------+--")
        print("   |     O")
        print("   |    /|")
        print("   |")
        print("   |")
        print("  ---")

    elif(wrong == 5):
        print("\n-------+--")
        print("   |     O")
        print("   |    /|\ ")
        print("   |")
        print("   |")
        print("  ---")

    elif(wrong == 6):
        print("\n-------+--")
        print("   |     O")
        print("   |    /|\ ")
        print("   |    /")
        print("   |")
        print("  ---")

    elif(wrong == 7):
        print("\n-------+--")
        print("   |     O")
        print("   |    /|\ ")
        print("   |    / \ ")
        print("   |")
        print("  ---")

name = input("Enter your name please >> ")

hangman()