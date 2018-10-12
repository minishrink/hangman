from enum import Enum

class GameState(Enum):
    IN_PROGRESS = 1
    WON = 2
    LOST = 3

class Hangman(object):

    UNKNOWN = '_'

    ### Object constructors and representations ###

    def __init__(self, answer, guesses_allowed):
        '''
        Hangman("answer", n) initialises a hangman game with the "answer",
        offering the player n guesses before failure
        '''
        self.guesses_left = guesses_allowed
        self._answer = answer
        self.word = [Hangman.UNKNOWN for c in answer]
        self.already_guessed = []
        self.result = GameState.IN_PROGRESS

    def __str__(self):
        return (' '.join(self.word))

    def __repr__(self):
        return ("Hangman({self._answer}, {self.guesses_left})".format(self = self))

    def remaining_guesses(self):
        print("You have {self.guesses_left} wrong guess(es) left.".format(self=self))


    ### Game guessing logic ###

    def no_guesses_left(self):
        return (self.guesses_left == 0)

    def wrong_guess(self, wrong):
        self.already_guessed.append(wrong)

    def update_word(self, guess):
        '''
        Update correctly guessed chars
        '''
        for i in range(len(self._answer)):
            if guess.lower() == self._answer[i].lower():
                self.word[i] = guess


    ### Game checking logic ###

    def player_won(self):
        return (self._answer.lower() == ''.join(self.word).lower())

    def final_result(self):
        if (self.result == GameState.WON):
            print("Congratulations, you win!")
        elif (self.result == GameState.LOST):
            print("Sorry, you lost. The correct answer was: {self._answer}".format(self=self))

    def update_state(self):
        '''
        Check if game has ended, then check if won or lost
        '''
        if self.player_won():
            self.result = GameState.WON
        elif self.no_guesses_left():
            self.result = GameState.LOST

    def get_state(self):
        '''
        Return whether game is IN_PROGRESS, has been WON or LOST
        '''
        return self.result

    def check_guess(self, guess):
        if guess.lower() in self._answer.lower():
            self.update_word(guess)
        else:
            self.wrong_guess(guess)
            self.guesses_left -= 1
            self.remaining_guesses()
        # this is where we check if the player has won
        self.update_state()

    def get_input(self):
        '''
        Sanitise input
        '''
        guess = str(input("Guess a letter: "))
        # if guess is not suitable
        while (guess.lower() in self.already_guessed or len(guess) != 1
                or guess.lower() in [c.lower() for c in self.word]):
            print("Guesses must be one character. Previously submitted guesses will not be counted.")
            guess = str(input("Guess a letter: "))
        return guess.lower()


    def guess(self):
        '''
        Player guesses a char, guess counter goes down, state is updated
        '''
        # sanitise input, discard previous guesses (correct or otherwise)
        guess = self.get_input()
        # update stored guesses, allowed guess counter, check if game over
        self.check_guess(guess)

    def play(self):
        while (not (self.no_guesses_left() or self.player_won())):
            self.guess()
            print("\n{}\n".format(self))
        self.final_result()

