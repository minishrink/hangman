from hangman import Hangman
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
    guesses = int(input("Enter maximum number of wrong guesses: "))
    return Hangman(word, guesses)

def main():
    game = make_game()
    game.play()

if (__name__=="__main__"):
    main()
