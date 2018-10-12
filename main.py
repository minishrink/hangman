from hangman import Hangman
import sys
from os import system, name

def secret_string():
    system("stty -echo")
    string = str(input())
    system("stty echo")
    print("\n")             # fix formatting
    return string

def hide_answer():
    print("Enter hangman answer: ")
    # windows system clear terminal
    if name == 'nt':
        word = str(input())
        _ = system('cls')
        return word
    # posix clear terminal
    elif name == 'posix':
        return secret_string()

def make_game():
    rules = """
    Start a game of Hangman by entering a word,
    then a max number of guesses the player is allowed before losing
    """
    print(rules)
    word = hide_answer()
    guesses = int(input("Enter max number of guesses: "))
    return Hangman(word, guesses)

def main():
    try:
        game = Hangman(sys.argv[1], int(sys.argv[2]))
    except:
        game = make_game()
    game.play()

if (__name__=="__main__"):
    main()
