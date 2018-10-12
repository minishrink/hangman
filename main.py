from hangman import Hangman
import sys
from os import system, name

def make_game():
    rules = """
    Start a game of Hangman by entering a word,
    then a max number of guesses the player is allowed before losing
    """
    print(rules)
    word = str(input("Enter a word: "))
    guesses = int(input("Enter max number of guesses: "))
    return Hangman(word, guesses)

def clear():
    # windows system clear terminal
    if name == 'nt':
        _ = system('cls')
    # posix clear terminal
    elif name == 'posix':
        _ = system('clear')

def main():
    try:
        game = Hangman(sys.argv[1], int(sys.argv[2]))
    except:
        game = make_game()
    clear()
    game.play()

if (__name__=="__main__"):
    main()
