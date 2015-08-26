""" Displays data for interaction with user"""
from itertools import zip_longest

class View:
    """ THis is how the game is presented to the player"""

    def __init__(self):
        """Init's view"""
        self.outcome = ""
        self.adjustment = -1


    def starting_print(self):
        """Print's rules """
        text = "Choose a column to drop your color checker."
        text += "Take turns for each move."
        text += "The object of the game is to get four of your color"
        text += "checkers either vertically, horizontally, or diagonally."
        print(text)


    def show_board(self, board):
        # print()
        # print(' ', end='')
        # for x in range(1, 8):
        #     print(' %s  ' % x, end='')
        # print()
        #
        # print('-----' + ('----' * (6)))
        #
        # for y in range(7):
        #
        #     print('|', end='')
        #     for x in range(6):
        #         print(' {} |'.format(board[x][y]), end='')
        #     print()
        #
        #     print('-----' + ('----' * (6)))
        """Prints the board to the users"""
        #prints it with an empty space
        #print(' ', end='')
       # print("  1   2   3   4   5   6   7")
        #for x in range(1, 7):
        #     print("  {}".format(x), end='')
        #print()

        # print('-----' + ('----' * (6)))
        #
        # for y in range(6):
        #    print('|', end='')
        #    for x in range(7):
        #        print(' %s |' % board[x][y], end='')
        #    print('-----' + ('----' * (6)))

        for col in range(6):
            print('  '.join(str(board[row][col]) for row in range(7)))
        print('--------------------')
        print('  '.join(map(str, range(1, 8))))

    #     """Appends whole row to grid"""
    #     for row in range(7):
    #         self.grid.append("_")
    #
    #     res = "|".join(self.grid)
    #
    #     #print(res)


    def show_turn(self, playing_player):
        """Print's the turn and asks for input"""

        inputNeeded = True
        players_move = 0
        while inputNeeded:
            # Prompt the user for their move
            players_move = input("Your turn, {}. What Column do you want to put your checker? (Please put in 1-7)"
                  .format(playing_player[0]))

            # Make sure that they give an int, and convert it to an int
            try:
                conversion = int(players_move)
            except ValueError:
                conversion = 8
                print("That's not a valid input.")

            # Check that it's in the range of 1-7
            if conversion not in range(1, 7):
                print("There is no column by that name.")
            else:
                inputNeeded = False
                players_move = conversion -1

        # Return the player's move choice
        return players_move

    def show_winner(self):
        """Print's if four in a row."""
        print(self.outcome)

    def show_tie(self):
        """Print's if no more spaces on board"""
        print("Yay! It's a tie! (^-^)")


