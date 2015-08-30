__author__ = 'Chelsea | Michael'

import unittest
from Conect4_Model import Model


class TestModelSwapPlayer(unittest.TestCase):
    """ Checks the model to see if the changing of the player is stored. """

    def setUp(self):
        """ Init's current player and players"""
        self.players = {1: ["Player_a", "x"], 2: ["Player_b", "o"]}
        self.test_function = Model()

    def tearDown(self):
        """ Closes the model """
        del self.test_function

    def test_change_to_player_a(self):
        """Testing if current player 1 gets self.players 1 value"""
        self.test_function.current_player = 1
        self.test_function.swap_player()
        self.assertEqual(self.test_function.current_player, 2)

    def test_change_to_player_b(self):
        """Testing if the current player 2 get self.player 2 value"""
        self.test_function.current_player = 2
        self.test_function.swap_player()
        self.assertEqual(self.test_function.current_player, 1)


if __name__ == '__main__':
    unittest.main()
