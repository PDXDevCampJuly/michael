"""
The Model stores the data and the logic to allow the Controller to access the data.
"""

class Model:
    """
    This class will hold the grid(list) and the players(Dict of lists).
    """

    def __init__(self):
        """This init's the class"""
        self.players = {1: ["Player_a", "\u25CF"], 2: ["Player_b", "\u25CB"]}
        self.current_player = 1
        self.playing_player = self.players[1]
        self.row = 6
        self.column = 7
        self.grid = [[" "] * 6 for x in range(7)]

    def update_board(self, move):
        """ Update the board based on players move. """
        #new_move equals the gird with selection(Which is the players input)
        new_move = self.grid[move]

        # check if column selected by player is full if the first index (top) has a game piece
        if new_move[0] != " " :
            return True

        # this will get the correct column and add the player's move
        # subtract player column selection by 1 to select correct column
        adjustment = -1
        while new_move[adjustment] != " ":
            adjustment -= 1

        # update the grid with the selected column by the player
        new_move[adjustment] = self.playing_player[1]
        return False

    def swap_player(self):
        """ This swaps the player from either player 1 or player 2. """

        # if player 1 then switch to player 2
        if self.current_player ==  1:
            self.current_player += 1
        else:
            self.current_player -= 1
        self.playing_player = self.players[self.current_player]
        return self.playing_player

