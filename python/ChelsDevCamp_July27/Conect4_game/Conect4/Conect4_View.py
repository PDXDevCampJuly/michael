""" The View displays data for interaction with user. """

from itertools import zip_longest

class View:
    """ This is how the game is presented to the player. """

    def __init__(self):
        """Init's the view. """
        self.outcome = ""
        self.adjustment = -1

    def starting_print(self):
        """ Prints the rules for the game. """
        text = "\nWelcome to Connect Four. The rules:"
        text += "\nChoose a column to drop the token of your color.\n"
        text += "Take turns for each move.\n"
        text += "The object of the game is to get four of your color\n"
        text += "tokens in a row either vertically, horizontally,\n"
        text += "or diagonally before the other player. Enjoy!\n"
        print(text)

    def show_board(self, board):
        """ Displays the current board. """
        print()
        print(" 1 2 3 4 5 6 7")
        for each_row in range(6):
             print("|", "|".join(column[each_row] for column in board), "|",sep='')
        print("---------------")
        print(" ^           ^ ")

    def show_turn(self, playing_player):
        """ Prints the turn and asks for input. """
        inputNeeded = True
        players_move = 0
        while inputNeeded:
            # Prompt the user for their move
            players_move = input("\nYour turn, {}.\n" \
                "Choose a column 1-7: "
                  .format(playing_player[0]))

            # Make sure that they give an int, and convert it to an int
            try:
                conversion = int(players_move)
            except ValueError:
                conversion = 8
                print("That's not a valid input. ")

            # Check that it's in the range of 1-7
            if conversion not in range(1, 8):
                print("There is no column by that name. ")
            else:
                inputNeeded = False
                players_move = conversion -1

        # Return the player's move choice
        return players_move

    def show_winner(self, playing_player):
        """Print's if four in a row exists. """
        print("Yay! {} won! (^-^)".format(playing_player))

    def show_tie(self):
        """ Print's if the board is full. """
        print("Yay! It's a tie! (^-^)")


