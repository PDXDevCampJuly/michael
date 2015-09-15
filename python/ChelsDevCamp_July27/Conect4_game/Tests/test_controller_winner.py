__author__ = 'Chelsea | Michael'

import unittest
from unittest.mock import patch
from Conect4_Controller import Controller
from io import StringIO

class TestControllerCheckWinner(unittest.TestCase):
    """ Checks the controller's logic for the situation of a win. """

    def setUp(self):
        """Inits empty grid for testing"""
        self.controller = Controller()

    def tearDown(self):
        """ Closes the view """
        del self.controller

    def test_if_winner_column_player_a(self):
        """ Check for a vertical win player A """

        self.controller.board = [
        [" "] * 6,
        [" "] * 6,
        [" "] * 6,
        [" "] * 6,
        [" "] * 6,
        [" "] * 2 + ["\u25CF"] * 4,
        [" "] * 6
        ]

        self.assertTrue(self.controller.check_winner())

    def test_if_winner_column_player_b(self):
        """ Check for a vertical win Player B """

        self.controller.board = [
        [" "] * 6,
        [" "] * 6,
        [" "] * 6,
        [" "] * 6,
        [" "] * 6,
        [" "] * 2 + ["\u25CB"] * 4,
        [" "] * 6
        ]

        self.assertFalse(self.controller.check_winner())

    def test_if_winner_row_player_A(self):
        """ Check for a horizontal win Player A """

        self.controller.board = [
        [" "] * 6,
        [" "] * 6,
        [" "] * 6,
        [" "] * 5 + ["\u25CF"] * 1,
        [" "] * 5 + ["\u25CF"] * 1,
        [" "] * 5 + ["\u25CF"] * 1,
        [" "] * 5 + ["\u25CF"] * 1,
        ]

        self.assertTrue(self.controller.check_winner())

    def test_if_winner_diag_player_a(self):
        """ Check for a diagonal win Player A """

        self.controller.board = [
        [" "] * 5 + ["\u25CF"] * 1,
        [" "] * 4 + ["\u25CF"] * 1 + [" "] * 1,
        [" "] * 3 + ["\u25CF"] * 1 + [" "] * 2,
        [" "] * 2 + ["\u25CF"] * 1 + [" "] * 3,
        [" "] * 1 + ["\u25CF"] * 1 + [" "] * 4,
        [" "] * 6,
        [" "] * 6
        ]

        self.assertTrue((self.controller.check_winner()))

    def test_if_winner_player_a_other_way(self):
        """ Check for other diagonal win Player A """

        self.controller.board = [
        [" "] * 6,
        [" "] * 6,
        [" "] * 1 + ["\u25CF"] * 1 + [" "] * 4,
        [" "] * 2 + ["\u25CF"] * 1 + [" "] * 3,
        [" "] * 3 + ["\u25CF"] * 1 + [" "] * 2,
        [" "] * 4 + ["\u25CF"] * 1 + [" "] * 1,
        [" "] * 5 + ["\u25CF"] * 1
        ]

        self.assertTrue((self.controller.check_winner()))

if __name__ == '__main__':
    unittest.main()
