""" Controller is the one class to rule them all! It's responsible for the comunication of model and view"""
from Conect4_View import View
from Conect4_Model import Model
import time

class Controller:
    """ Creates logic for comunication model and view"""

    def __init__(self):
        """ Inti's controller"""
        # self.current_board = self.something_model.make_board()
        # print(self.current_board)
        #self.current_move = self.View.current_play
        self.view = View()
        self.model = Model()
        self.board = self.model.grid


    def get_board_status(self):
        """ Takes input from grid and updates view"""
        self.board = self.model.grid
        self.view.show_board(board)


    def get_move(self):
        """Get's the inout from the view and puts it into model"""
        move_needed = True

        while move_needed:
            move = self.view.show_turn()

            move_needed = self.model.update_board(move)


    def check_tie(self):
        """ Loops through the board and looks for a empty space. If it does find a space it print's that it was a tie
        and exits"""
        # for x in self.board: # loop through each inner list
        #     for each_index in x: # loop through each index of inner lists
        #         if each_index[0] == " ":
        #         else:
        #             self.view.show_tie()
        #             print("If there anybody home?")
        #             exit()
        pass


    def check_winner(self):
        """ Checks to see if four in a row"""
        for x in self.board:
            for each_index in x:
                pass

    def main(self):
        """ Starts game and calls all helper functions"""
        self.model.make_board()
        print(self.model.grid)
        self.get_move()
        print(self.board)

