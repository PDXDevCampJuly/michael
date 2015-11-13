__author__ = 'Chelsea | Michael'

import unittest
from Conect4_Model import Model
from unittest.mock import patch


class TestModelUpdateBoard(unittest.TestCase):
    """ Checks the model to see if the board changes are stored. """

    def setUp(self):
        """ Init's current player and players"""
        self.model = Model()

    def tearDown(self):
        """ Closes the model """
        del self.model

    def test_userinput_changes_board_5pieces (self):
        """ Test for a vertical board update index 5 and 5 pieces"""

        self.model.update_board(5)

        mock_board = [
        [" "] * 6,
        [" "] * 6,
        [" "] * 6,
        [" "] * 6,
        [" "] * 6,
        [" "] * 5 + ["\u25CF"],
        [" "] * 6
        ]

        self.assertEqual(self.model.grid, mock_board, "Column did not update")

    def test_userinput_changes_board_six_pieces (self):
        """ Test for a vertical board update index 5 and six pieces """

        self.model.grid = [
        [" "] * 6,
        [" "] * 6,
        [" "] * 6,
        [" "] * 6,
        [" "] * 6,
        ["\u25CF"] * 6,
        [" "] * 6
        ]

        column_full = self.model.update_board(5)
        self.assertTrue(column_full, "Board said column was not full")

    def test_userinput_changes_board_differences(self):
        """ Test differences in the boards and full column """

        self.model.grid = [
        [" "] * 6,
        [" "] * 6,
        [" "] * 6,
        [" "] * 6,
        [" "] * 6,
        [" "] * 3 + ["\u25CF"] * 3,
        [" "] * 6
        ]

        column_full = self.model.update_board(5)

        mock_board = [
        [" "] * 6,
        [" "] * 6,
        [" "] * 6,
        [" "] * 6,
        [" "] * 6,
        [" "] * 2 + ["\u25CF"] * 4,
        [" "] * 6
        ]

        self.assertFalse(column_full, "Board said column was full")
        self.assertEqual(self.model.grid, mock_board, "Column did not update")


if __name__ == '__main__':
    unittest.main()
