from hangman import Hangman

def make_game():
    rules = """
    Start a game of Hangman by entering a word,
    then a max number of guesses the player is allowed before losing
    """
    print(rules)
    word = str(input("Enter a word: "))
    guesses = int(input("Enter max number of guesses: "))
    return Hangman(word, guesses)

import sys

def main():
    try:
        game = Hangman(sys.argv[1], int(sys.argv[2]))
    except:
        game = make_game()
    game.play()

if (__name__=="__main__"):
    main()
