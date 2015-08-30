"""
Controller is the one class to rule them all! It's responsible for the communication of model and view
"""

from Conect4_View import View
from Conect4_Model import Model
from itertools import product

class Controller:
    """ Creates logic for communication model and view. """

    def __init__(self):
        """ Init's controller"""
        self.winner = False
        self.view = View()
        self.model = Model()
        self.board = self.model.grid

    def get_board_status(self):
        """ Takes input from grid and updates view for display. """
        self.board = self.model.grid
        self.view.show_board(self.board)

    def get_move(self):
        """
        Get's the input from the view and stores it in the update_board in the model.
        """
        move_needed = True

        while move_needed:
            move = self.view.show_turn(self.model.playing_player)

            move_needed = self.model.update_board(move)

    def check_tie(self):
        """
        Loops through the board and looks for a empty space. If it does find a space it print's that it was a tie.
        """
        for x in self.board: # loop through each inner list
            if x[0] == " ":
                return False
        self.view.show_tie()
        return True

    def check_winner(self):
        """
        Checks to see if four in a row exists horizontally, vertically, or diagonally. """
        for x in self.board:
            if self.model.playing_player[1] * 4 in "".join(x):
                return True

        for each_row in range(6):
            if self.model.playing_player[1] * 4 in "".join(column[each_row] for column in self.board):
                return True

        for row, column in product(range(5,2, -1), range(4)):
            if self.model.playing_player[1] * 4 in "".join(self.board[column + i][row - i] for i in range(4)):
                return True

        for row, column in product(range(3), range(4)):
            if self.model.playing_player[1] * 4 in "".join(self.board[column + i][row + i] for i in range(4)):
                return True

        return False

    def main(self):
        """
        Starts game and calls all helper functions to control the flow of the game.
        """
        winner = False
        self.view.starting_print()
        while winner == False:
            self.view.show_board(self.board)
            self.get_move()
            winner = self.check_winner()
            if winner:
                self.view.show_board(self.board)
                self.view.show_winner(self.model.playing_player[0])
                break
            winner = self.check_tie()
            if winner:
                self.view.show_board(self.board)
                self.view.show_tie(self.model.playing_player[0])
            self.model.swap_player()


if __name__ == '__main__':
    game = Controller()
    game.main()
